from django.db import models
import uuid
from users.models import Profiles

# Create your models here.
class postform(models.Model):
    owner = models.ForeignKey( Profiles, on_delete=models.CASCADE, null=True, blank=True)
    jobrole = models.CharField(max_length=200)
    companyname = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    discription = models.TextField(null=True,blank=True)
    source_link = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.jobrole
    
    
class posteventform(models.Model):
    eventname = models.CharField(max_length=200)
    organiser = models.CharField(max_length=200)
    discription = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    last_date = models.DateTimeField(auto_now_add=False ,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.eventname
    
