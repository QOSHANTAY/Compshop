from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User 
from django.forms import ModelForm
from django import forms
from .models import Comment

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {forms.Textarea(
            attrs = {
                'placeholder':'Here you should write comments:',
                'class':'form-control',
                'rows':3
            }
        )}