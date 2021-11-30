from django import forms
from django.forms import ModelForm,fields, models
from django.contrib.auth.models import User,auth
class UserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"