
from django import forms
from .models import Login


class LoginForm (forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        # choose all fields from model
        # fields = ['username']
        # choose specific fields
        



    
    



