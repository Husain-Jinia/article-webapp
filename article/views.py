from re import template
from .models import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import  DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
@login_required 
def articleCreation(request):
    form = ArticleCreationForms(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.cleaned_data)
            print(str(form.cleaned_data))
            print("here")
    
    return render(request, 'articleCreationpage.html', {'form':form})


def dashboard(request):
    articles = Articles.objects.all()
    return render(request,'dashboard.html',{"articles":articles})

@login_required
def viewArticle(request):
    user_post = Articles.objects.filter(author = request.user)
    return render(request, 'articleView.html',{'user_post':user_post})

class DeleteArticle(DeleteView):
    model = Articles
    template_name = 'deleteArticle.html'
    success_url = reverse_lazy(viewArticle)

class UpdateArticle(UpdateView):
    model = Articles
    template_name = 'updateArticle.html'
    fields = ['title','description','image','category']
    success_url = reverse_lazy(viewArticle)
    