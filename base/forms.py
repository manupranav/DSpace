from attr import field, fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields= ['name','username', 'email','password1','password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['participants','host']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','avatar','bio','username', 'email']