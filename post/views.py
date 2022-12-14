from django.shortcuts import render ,redirect
from django.http import HttpResponse
from post.models import postform
from post.models import posteventform
from post.forms import postforms,posteventforms
from users.models import Profiles
# Create your views here

def Postform(request):
    form = postforms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('postformdetails')
    context = {'form':form}
    return render(request, 'post/post_form.html', context)

def postformdetails(request):
    # proff2 = Profiles.objects.all()
    proff = postform.objects.all()
    context = {"details":proff}
    return render(request, 'post/post.html',context)



def postevent(request):
    proffs = posteventform.objects.all()
    context = {"eventdetail":proffs}
    return render(request, 'post/events.html',context)

def posteventkaform(request):
    form = posteventforms(request.POST)
    if form.is_valid():
        form.save();
        redirect('postevent')
    context = {'form':form}
    
    return render(request, 'post/post_event_form.html',context)