from django import forms
from django.contrib.auth.models import User
from Vendor.models import Vendormod

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']

class insert_new_vendorform(forms.ModelForm):
    class Meta:
        model=Vendormod
        fields='__all__'
