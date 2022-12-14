# '''
#   signals--->
  
  
  
#   *three main things  1-sender  2-signal  3-receiver
#   *main signal is post_save
  
#   *to apply signal  
#      import following modeules in signals.py
#     a-from .models import Profile    #taking profile as model
#     b-from django.contrib.auth.models import User
#     c-from django.dispatch import receiver(for connection)
    
#   *add following code in apps.py file-
  
#       def ready(self):
#             import alumni.signals  #taking alumni as my app
            
            
#      AND
#    * add following path in setting.py installed app secions-
#        'alumni.apps.AlumniConfig',  #taking alumni as my app

# '''



# from django.db.models.signals import post_save
# from users.models import Profiles
# from django.contrib.auth.models import User
# from django.dispatch import receiver



# @receiver(post_save,sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profiles.objects.create(user=instance)
#         print("profile created")
        
# post_save.connect(create_profile,sender=User)


# @receiver(post_save,sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#        instance.save()
#        print("profile updated")
       
# post_save.connect(update_profile,sender=User)