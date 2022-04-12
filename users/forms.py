from pyexpat import model
from statistics import mode
from unittest.mock import mock_open
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from django import forms
from .models import Profile, Interests

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'email': 'Email',
        }


# class MyCustomSignupForm(SignupForm):
#     # def __init__(self, *args, **kwargs):
#     #     super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#     #     self.fields['name'] = forms.CharField(required=True)
#     # def save(self, request):
#     #     name = self.cleaned_data.push('Name')
        
#     #     user = super(MyCustomSignupForm, self).save(request)

#     #     return user



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'profile_image', 'github', 'twitter']


class InterestForm(ModelForm):
    class Meta:
        model = Interests
        fields = "__all__"
        exclude =['owner']
    
    def __int__(self, *args, **kwargs):
        super(InterestForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
