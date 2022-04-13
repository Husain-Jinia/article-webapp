from .models import *
from django import forms

class ArticleCreationForms(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ("title","description","image","author","category","posted_on")
