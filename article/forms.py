from .models import *
from django import forms

class ArticleCreationForms(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ("title","description","image","author","category","posted_on")
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'description': forms.Textarea(attrs={'class':'form-control py-2'}),
            'author' : forms.Select(attrs={'class':'form-control py-2'}),
            'category' : forms.Select(attrs={'class':'form-control py-2'}),
        }

class ArticleUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ("title","description","image","category")
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'description': forms.Textarea(attrs={'class':'form-control py-2'}),
            'category' : forms.Select(attrs={'class':'form-control py-2'}),
        }
