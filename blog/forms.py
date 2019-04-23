from django import forms
from .models import Post 

class PostForm(forms.ModelForm):
    #Tell django what to make form out of ??? 
    class Meta:
        model = Post
        fields = ('title', 'text')