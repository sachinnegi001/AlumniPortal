from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages                         #to import the messages functionality
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, logout,login, update_session_auth_hash #to update for every logout  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .models import contact,Profile,Studentprofile
from django.dispatch import Signal, receiver
from django.core.validators import validate_email




# Create your views here.
def index(request):
       return render(request, 'alumni/index.html')
 
 

def studentdashbord(request):
      
      if request.user.is_authenticated:
            
            profile = Studentprofile.objects.get(user__id=request.user.id)
         
                  
            return render(request, 'alumni/studentdashbord.html',{"proflie":profile})
      else:
            return HttpResponseRedirect('/errorpage')
  
@login_required
def alumnidashbord(request):

            return render(request, 'alumni/alumnidashbord.html')
  

def error(request):
      return render(request, 'alumni/error.html')



def contactpage(request):
      if request.method == 'POST':
            nm = request.POST['name']
            em = request.POST['email']
            sub = request.POST['subject']
            mes = request.POST['message']
            
            data = contact(name=nm,email=em,subject=sub,Message=mes)
            try:
                validate_email(em)
            except :
                return HttpResponseRedirect('/errorpage')
            else:
             data.save()
            
            res = "Dear {} Thankyou For Your Response ".format(nm)
            return render(request, 'alumni/contact.html',{"status":res})
            # return HttpResponse('<h1>Dear {} Thankyou For Your Response </h1>'.format(nm))
      return render(request, 'alumni/contact.html')      






def adminsite(request):
      proff = contact.objects.all().order_by("-id")    #to show the reccent data in first .order_by("name") to show alphabetically
      context = {"profile":proff,'lenght':len(proff)} 
      return render(request, 'alumni/database.html',context)      
  
       
      
@login_required()
def studentprofilepage(request):
            profile = Studentprofile.objects.get(user__id=request.user.id)
            context = {'proff':profile}
            return render(request, 'alumni/alumniprofile_page.html',context)
      
@login_required()
def alumniprofilepage(request):
            profile = Profile.objects.get(user__id=request.user.id)
            context = {'proff':profile}
            return render(request, 'alumni/alumniprofile_page.html',context)
      
def editprofilestudent(request):
      return render(request, 'alumni/editprofilestudent.html') 
def editprofilealumni(request):
      if request.method == 'POST':
          
            picture = request.POST.get("picture")
            fathername = request.POST.get("fathername")
            mothername = request.POST.get("mothername")
            city = request.POST.get("city")
            state = request.POST.get("state")
            email = request.POST.get("email")
            dateofbirth = request.POST.get("dateofbirth")
            phonenumber = request.POST.get("phonenumber")
            gender = request.POST.get("gender")
            currentaddress = request.POST.get("currentaddress")
            permanentaddress = request.POST.get("permanentaddress")
            jobprofile = request.POST.get("jobprofile")
            joblocation = request.POST.get("joblocation")
            companyname = request.POST.get("companyname")
            skill = request.POST.get("skill")
            bio = request.POST.get("bio")
            
            profile=Profile(picture=picture,fathername=fathername,
                              mothername=mothername,
                              city=city,
                              state=state,
                              email=email,
                              dateofbirth=dateofbirth,
                              phonenumber=phonenumber,
                              gender=gender,
                              currentaddress=currentaddress,
                              permanentaddress=permanentaddress,
                              jobprofile=jobprofile,
                              joblocation=joblocation,
                              companyname=companyname,
                              skill=skill,
                              bio=bio)
            profile.save()
            
            return render(request, 'alumni/editprofilealumni.html') 
           
           
      
      return render(request, 'alumni/editprofilealumni.html') 
 
 
 
 
 ## profile details page-
'''
def profiledetailspage(request):
      if request.method == 'POST':                  # here if we post the request or request is post after submitting
       fm = profiledetailsform(request.POST)       #the fm a object were all data come from form (studentregistration)
       if fm.is_valid():#validation of the data
        fm.save()#save our data
        return HttpResponseRedirect('profilepage')  #shows us a blank form after adding data
      else:
        fm = profiledetailsform()
      return render(request, 'Blog/profiledetails.html', {'form':fm})
'''  

def signin(request):
      if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
  
            user=auth.authenticate(username=username,password=password)
            if user:
                  login(request, user)  
                  if user.is_superuser:
                        return HttpResponseRedirect("/adminn")
                  elif user.is_staff:
                        return HttpResponseRedirect("/alumnidashbord")
                  elif user.is_active:
                        return HttpResponseRedirect("/studentdashbord")
                 
            else:
                 
                  return render(request, 'alumni/signin.html',{"status":"invalid credentials"})
      else: 
       return render(request, 'alumni/signin.html')


def signup(request):
      
      if request.method=='POST':
       
        username=request.POST['username']
        email=request.POST['emailid']
        password1=request.POST['password1']
        password2=request.POST['password2']
        typ= request.POST['utype']
        
        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                  messages.info(request,"the username is already taken.....")
                  return redirect('signup')
            
            elif User.objects.filter(email=email).exists():
                  messages.info(request,"the email-id is already registered.....")
                  return redirect('signup')
            else:
                  usr = User.objects.create_user(username=username,email=email,password=password1)
                  if typ =="alumni":
                        usr.is_staff = True
                  elif typ=="teacher":
                        usr.is_staff = True
                  
                  usr.save()
                  
                  if usr.is_staff:
                        reg = Profile(user=usr,email=email)
                        reg.save()
                        messages.info(request,"your account has been created sucessfully....")
                  else:
                        regg = Studentprofile(user=usr,email=email)
                        regg.save()    
            return redirect("signin")
      
        else:
            messages.info(request,"the passwords are not matched.....")
        return redirect('signup')

    
            
      return render(request, 'alumni/signup.html')
 


def logout_user(request):
    logout(request)
   
    return  HttpResponseRedirect('/')
 
# change password with old password
       
def changepass(request):
      if request.user.is_authenticated:
            if request.method == "POST":
                  fm=PasswordChangeForm(user=request.user,data=request.POST)
                  if fm.is_valid():
                        fm.save()
                        update_session_auth_hash(request,fm.user)
                        messages.info(request, 'Your Passwor is sucessfully changed...')
                        return HttpResponseRedirect('userdashbord')
            else:
                  fm=PasswordChangeForm(user=request.user)
            return render(request, 'alumni/changepassword.html',{'form':fm})
      else:
       return HttpResponseRedirect('signin')  

  
  

    
