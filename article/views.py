from pdb import post_mortem
from re import template
from users.models import *
import article
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import  CreateView,DeleteView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy, reverse

# Create your views here.

def likeView(request, pk,*args,**kwargs):
    article = Articles.objects.get(pk=pk)
    disliked = False
    for dislike in article.dislikes.all():
        if dislike == request.user:
            disliked = True
            break
    if disliked:
        article.dislikes.remove(request.user)

    liked = False
    
    for like in article.likes.all():
        if like == request.user:
            liked == True
            break
    if not liked:
        article.likes.add(request.user)
    if liked:
        article.likes.remove(request.user)

    next  = request.POST.get('next','/dashboard')
    return HttpResponseRedirect(next)

def dislikeView(request,pk,*args,**kwargs):
    article = Articles.objects.get(pk=pk)
    liked = False
    
    for like in article.likes.all():
        if like == request.user:
            liked = True
            break
    
    if liked:
        article.likes.remove(request.user)

    disliked = False
    for dislike in article.dislikes.all():
        if dislike == request.user:
            disliked = True
            break
    if not disliked:
        article.dislikes.add(request.user)
    if disliked:
        article.dislikes.remove(request.user)


    next  = request.POST.get('next','/dashboard')
    return HttpResponseRedirect(next)



class ArticleCreation(CreateView):   
    model=Articles
    form_class = ArticleCreationForms
    template_name='articleCreationpage.html'


def dashboard(request):
    print(request.user)
    if request.user.is_authenticated:
        profile= Profile.objects.filter(user=request.user).first()
        categories = profile.category.all()
        articles=[]
        for category in categories:
            articles+= Articles.objects.filter(category=category)

        
        return render(request,'dashboard.html',{'articles':articles, 'categories':categories})
    else:
        return render(request,'dashboard.html')
    
class ArticleDetailView(DetailView):
    model= Articles
    template_name = 'articleDetails.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        return context
    

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
    form_class = ArticleUpdateForm
    template_name = 'updateArticle.html'
    success_url = reverse_lazy(viewArticle)
    

