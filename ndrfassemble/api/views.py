from calendar import c
import profile
from django.http import response
from .serializers import  Profileserializer, FeedDataModelSerializer
from rest_framework.response import Response
from .models import Profile, FeedDataModel
from rest_framework.decorators import api_view
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.mail import send_mail


@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def logininfo(request):
    if request.method == 'GET':
        orders = Profile.objects.filter(username = request.data['username']).values_list('id', flat=True)
        data = {}
        data['id'] = orders[0]
        return Response(data)


@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def Profilegetpost(request):
    if request.method == 'GET':#for all users
        users = Profile.objects.all()
        serializer = Profileserializer(users,many = True)
        return Response(serializer.data)
        
    if request.method == 'POST': #get single user
        serializer  = Profileserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['DELETE'])
def deleteUser(request,pk):
    if request.method == 'DELETE': #delete user
        Profile.objects.get(pk=pk).delete()
        return Response(status = 200)
        


@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def getsingleuserdata(request, pk):   #single user data
    if request.method == 'GET':
        userdata = Profile.objects.get(pk = pk)
        serializer = Profileserializer(userdata)
        return Response(serializer.data)


#userdata api ends here

@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def FeedGetPostData(request):
    if request.method == 'GET':
        orders = FeedDataModel.objects.all()
        serializer = FeedDataModelSerializer(orders,many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer  = FeedDataModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['DELETE'])
def deletefeedData(request,pk):
    if request.method == 'DELETE': #delete feed data
        FeedDataModel.objects.get(pk=pk).delete()
        return Response(status = 200)



@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def getsinglefeedinfo(request, pk):   #single user data
    if request.method == 'GET':
        userdata = FeedDataModel.objects.get(pk = pk)
        serializer = FeedDataModelSerializer(userdata)
        print(serializer.data)
        return Response(serializer.data)



@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def VolunteerJoinEventApi(request,userid, pk):   #single user data
    if request.method == 'GET':
        userdata = FeedDataModel.objects.get(pk = pk)
        serializer = FeedDataModelSerializer(userdata)
        attendiesprev = serializer.data['attendies']
        print("##########", attendiesprev)
        FeedDataModel.objects.filter(pk=pk).update(attendies=attendiesprev+ "@"+ userid)

        return Response(serializer.data)



@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def eventattendiesdata(request, pk):   #single user data
    if request.method == 'GET':
        userdata = FeedDataModel.objects.get(pk = pk)
        serializer = FeedDataModelSerializer(userdata)
        attendiesprev = serializer.data['attendies']
        if(attendiesprev==""):
            return Response(status = 200)
        index = []
        index = attendiesprev.split("@")
        finalres = {}
        for i in index:
            userdata = Profile.objects.get(pk = pk)
            finalres[i] = Profileserializer(userdata).data
        return Response(finalres)





@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def sendmail(request):
    if request.method == 'GET':
        emaillist = Profile.objects.all().values_list('email', flat=True)
        print(emaillist)
        send_mail(
        subject='Need help on your event',
        message='Hello please open your ndrf assemble app we need your help',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emaillist)
    
    return Response(status = 200)
