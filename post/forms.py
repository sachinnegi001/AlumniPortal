from django.forms import ModelForm
from post.models import postform , posteventform



class postforms(ModelForm):
    class Meta:
        model = postform
        fields = '__all__'
        
        
class posteventforms(ModelForm):
    class Meta:
        model = posteventform
        fields = '__all__'
        

