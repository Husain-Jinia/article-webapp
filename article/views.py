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

        print(articles)
        return render(request,'dashboard.html',{'articles':articles})
    else:
        return render(request,'dashboard.html')

    # liked = False
    # if articles.likes.filter(id = request.user.id).exists():
    #     liked =True
    


class ArticleDetailView(DetailView):
    model= Articles

    template_name = 'articleDetails.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Articles, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked=False
        if stuff.likes.filter(pk = self.request.user.pk).exists():
            liked = True
        context["total_likes"] = total_likes 
        context["liked"] = liked
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
    

def likeView(request, pk):
    article = get_object_or_404(Articles,pk=request.POST.get('article_id'))
    print("ssssssssssssssssssssssssssssssssssss",article)
    liked = False
    if article.likes.filter(pk=request.user.pk).exists():
        article.likes.remove(request.user)
        liked=False
    else:
        article.likes.add(request.user)
        liked=True
    
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
