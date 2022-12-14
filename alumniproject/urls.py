"""blogweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from alumni import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('adminn/', admin.site.urls),
    path('', views.index,name='index'),
    path('users/', include('users.urls')), 
    path('post/', include('post.urls')),
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('contact/', views.contactpage,name='contact'),
    path('adminsite/', views.adminsite,name='adminsite'),
    path('errorpage/',views.error,name='error'),
    
    path('studentdashbord/',views.studentdashbord,name='studentdashbord'),
    path('alumnidashbord/',views.alumnidashbord,name='alumnidashbord'),
    path('alumniprofilepage/',views.alumniprofilepage,name='alumniprofilepage'),
    path('studentprofilepage/',views.studentprofilepage,name='studentprofilepage'),
    path('logout',views.logout_user,name='logout'),
    # path('changepass',views.changepass,name='changepass'),
     path('editprofilealumni',views.editprofilealumni,name='editprofilealumni'),
     path('editprofilestudent',views.editprofilestudent,name='editprofilestudent'),
   
  
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
