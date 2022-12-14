from django.contrib import admin
from post.models import postform
from post.models import posteventform

# Register your models here.
admin.site.register(postform)
admin.site.register(posteventform)