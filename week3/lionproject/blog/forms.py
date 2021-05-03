from django import forms
from .models import Post

class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']