from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields=("username","password1","password2",)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)
        widgets = {'text' : SummernoteWidget}

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)