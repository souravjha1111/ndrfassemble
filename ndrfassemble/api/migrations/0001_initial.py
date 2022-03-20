# Generated by Django 3.1.5 on 2022-03-20 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=22)),
                ('generallocation', models.CharField(max_length=100)),
                ('currentlocation', models.CharField(max_length=100)),
                ('verification_id', models.ImageField(blank=True, upload_to='images')),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeedDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('assemblelocation', models.CharField(max_length=100)),
                ('disisterlocation', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timing', models.DateTimeField(default=datetime.datetime(2022, 3, 20, 16, 5, 48, 603549, tzinfo=utc))),
                ('typeofalert', models.BooleanField(default=False)),
                ('attendies', models.CharField(blank=True, max_length=100, null=True)),
                ('postedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
    ]