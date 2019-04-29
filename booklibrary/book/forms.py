from django import forms
from .models import Suser


class SuserForm(forms.ModelForm):
    class Meta():
        model = Suser
        fields = ['username','password','college','uno','email']

# class SLoginForm(forms.ModelForm):
#     class Meta():
#         model = Suser
#         fields = ['username','password']


