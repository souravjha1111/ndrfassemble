from django.db import models
from datetime import datetime
from statistics import mode
import django
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid
import datetime


class Profile(models.Model):
    username = models.CharField(max_length=100, blank=False)
    phone_number = models.IntegerField(default=0, blank=False)
    age = models.IntegerField(default=22, blank=False)
    generallocation = models.CharField(max_length=100, blank=False)
    currentlocation = models.CharField(max_length=100, blank=False)
    verification_id = models.ImageField(blank = True, upload_to='images')
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class FeedDataModel(models.Model):
    postedby = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    assemblelocation = models.CharField(max_length=100)
    disisterlocation = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    timing = models.DateTimeField(default=django.utils.timezone.now())
    typeofalert = models.BooleanField(default=False)
    attendies  = models.CharField(max_length=100, default = "" ,blank=True, null=True)
    def __str__(self):
        return f'{self.postedby.id} FeedDataModel'






# class worker(models.Model):
#     workerid = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     jobaccepted = models.ForeignKey(jobpost, on_delete=models.CASCADE)
#     jobstatus = models.BooleanField(default=True)
#     paymentstatus = models.BooleanField(default=False)
#     acceptedtiming = models.DateTimeField(default=django.utils.timezone.now())

#     def __str__(self):
#         return f'{self.workerid.username} Worker'