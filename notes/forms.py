from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.models import User
from .models import Classes,Notes


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password',)

class NoteForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ('title','note_image')
