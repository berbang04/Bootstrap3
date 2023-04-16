from django import forms
from django.core import validators
from .models import BlogPost
from tinymce.widgets import TinyMCE

class PostModelForm(forms.ModelForm):
    tag=forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 20, 'rows': 10}))
    title=forms.CharField(validators=[validators.MinLengthValidator(3)])
    
    class Meta:
        model = BlogPost
        fields = [
            "title", 
            "cover_image",
            "content",
            "category",
            "tag",
            ]