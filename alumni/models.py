from django.db import models
from django.contrib.auth.models import User   #we are importing default User Model through authentication


    
class Profile(models.Model):
    
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE) # Delete profile when user is deleted
    picture=models.ImageField(default='default.jpg',upload_to="myimage" ,null=True)
    fathername=models.CharField(max_length=500, null=True)
    mothername=models.CharField(max_length=500, null=True)
    city=models.CharField(max_length=20, null=True)
    state=models.CharField(max_length=20, null=True)
    email=models.CharField(max_length=200,null=True)
    dateofbirth=models.DateField( null=True)
    phonenumber=models.IntegerField(null=True)
    gender=models.CharField(max_length=10, null=True)
    currentaddress=models.CharField(max_length=100, null=True)
    permanentaddress=models.CharField(max_length=100, null=True)
    jobprofile=models.CharField(max_length=20, null=True)
    joblocation=models.CharField(max_length=20, null=True)
    companyname=models.CharField(max_length=20, null=True)
    skill=models.TextField(max_length=500, null=True)
    bio=models.TextField(max_length=500, null=True)

    def __str__(self):
            return str(self.user) #show how we want it to be displayed
        #it only desplay string value so if we want to desplay any of integer value so we have to assign in to string value by str()


class Studentprofile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    fathername = models.CharField( max_length=50)    
    mothername = models.CharField( max_length=50)    
    city = models.CharField( max_length=50)    
    state = models.CharField( max_length=50)    
    rollnumber = models.IntegerField(null=True)
    stream = models.CharField( max_length=200)
    email = models.EmailField( max_length=254)
    dob = models.DateField(null=True)
    phonenumber = models.IntegerField(null=True)
    address = models.TextField(max_length=200)
    skills = models.TextField(max_length = 200)

    def __str__(self):
        return str(self.user)
    
        
class contact(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    subject= models.CharField(max_length=200)
    Message= models.TextField()
    
    def __str__(self):
        return str(self.name)
    

