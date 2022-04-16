from logging import PlaceHolder
from .models import *
from django import forms
from users.models import Profile

class ArticleCreationForms(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ("title","description","image","author","category","posted_on")
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'description': forms.Textarea(attrs={'class':'form-control py-2'}),
            'author' : forms.TextInput(attrs={'class':'form-control py-2','value':'','id':'elder',"type":"hidden"}),
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

class UpdateCategoryPreferenceForm(forms.ModelForm):
    model = Profile
    fields = ("category")