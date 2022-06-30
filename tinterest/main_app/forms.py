from django.forms import ModelForm
from .models import Profile, User
from django import forms

class ProfileForm(ModelForm): 
    class Meta: 
        model = Profile
        fields = ['image', 'about', 'website']
        

# class ProfileForm(forms.Form): 
#     bio = forms.CharField(default="default value"), 
#     url = forms.URLField(label='Website', required=False)
      
    
class UserForm(ModelForm): 
    class Meta: 
        model = User
        fields = ['username']