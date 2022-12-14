from django.db import models
from django.contrib.auth.models import User   #we are importing default User Model through authentication
import uuid
# Create your models here.
'''
Basically we are creating our custom models here

'''

    
class Profiles(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE,blank=True) # Delete profile when user is deleted
    picture=models.ImageField(default='userimages/default.jpg',upload_to="userimages/" ,null=True,blank=True)
    fathername=models.CharField(max_length=500, null=True,blank=True)
    mothername=models.CharField(max_length=500, null=True,blank=True)
    city=models.CharField(max_length=20, null=True,blank=True)
    state=models.CharField(max_length=20, null=True,blank=True)
    email=models.EmailField(max_length=500,blank=True,null=True)
    dateofbirth=models.DateField( null=True,blank=True)
    phonenumber=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=10, null=True,blank=True)
    currentaddress=models.CharField(max_length=100, null=True,blank=True)
    permanentaddress=models.CharField(max_length=100, null=True,blank=True)
    jobprofile=models.CharField(max_length=20, null=True,blank=True)
    joblocation=models.CharField(max_length=20, null=True,blank=True)
    companyname=models.CharField(max_length=20, null=True,blank=True)
    skill=models.TextField(null=True,blank=True)
    bio=models.TextField( null=True,blank=True)
    social_github=models.CharField(max_length=200,blank=True,null=True)
    social_linkedin=models.CharField(max_length=200,blank=True,null=True)
    social_twitter=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    

    
    def __str__(self):
            return str(self.user) #show how we want it to be displayed
        
        
    
