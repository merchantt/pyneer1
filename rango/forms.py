from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):

    keyword1 = forms.CharField(required=False)
    keyword2 = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)
