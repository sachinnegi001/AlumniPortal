from django.shortcuts import render
from.models import Profiles
# Create your views here.

def userdashbord(request):
    return render(request, 'users/userdashbord.html')

def userposts(request):
    prof = Profiles.objects.all()
    context = {'profile':prof}
    return render(request, 'users/userposts.html',context)


def user_profile(request,pk):
    
    profile = Profiles.objects.get(id=pk)
    context = {'proff':profile}
    return render(request, 'users/profile_page.html',context)