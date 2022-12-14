from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    
   path('postform',views.Postform,name='Postform') ,
   path('postformdetails',views.postformdetails,name='postformdetails') ,
   path('postevent',views.postevent,name='postevent') ,
   path('posteventkaform',views.posteventkaform,name='posteventkaform')
   
   
]