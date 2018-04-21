from django.contrib.auth.models import User
from django import forms
from django.http import request


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ContactForm(forms.Form):
    from_email = forms.CharField(initial='Registered_Email', disabled=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)