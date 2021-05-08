from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    STATUS_CHOICES = (('user','User'),('vendor','Vendor'))
    phone = forms.CharField()
    role = forms.ChoiceField(choices=STATUS_CHOICES)
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password','phone','role']
        