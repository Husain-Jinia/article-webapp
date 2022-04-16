from re import template
from users.models import *
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import  CreateView,DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy



# Functional view created to display all the articles based on user preference
def dashboard(request):
    print(request.user)
    if request.user.is_authenticated:
        # fetching articles based on user prefered categories
        profile= Profile.objects.filter(user=request.user).first()
        categories = profile.category.all()
        articles=[]
        for category in categories:
            articles+= Articles.objects.filter(category=category)

        
        return render(request,'dashboard.html',{'articles':articles, 'categories':categories})
    else:
        return render(request,'dashboard.html')

# Class based view to display the detailed view for the article
class ArticleDetailView(DetailView):
    model= Articles
    template_name = 'articleDetails.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        return context

# Class based view for users to write their own articles
class ArticleCreation(CreateView):   
    model=Articles
    form_class = ArticleCreationForms
    template_name='articleCreationpage.html'


# Functional view for user to view their own articles
@login_required
def viewArticle(request):
    user_post = Articles.objects.filter(author = request.user)
    return render(request, 'articleView.html',{'user_post':user_post})

# Class based view created for users to delete their own articles
class DeleteArticle(DeleteView):
    model = Articles
    template_name = 'deleteArticle.html'
    success_url = reverse_lazy(viewArticle)

# Class based view created for users to update their own articles
class UpdateArticle(UpdateView):
    model = Articles
    form_class = ArticleUpdateForm
    template_name = 'updateArticle.html'
    success_url = reverse_lazy(viewArticle)


# Like functionality
def likeView(request, pk,*args,**kwargs):
    
    article = Articles.objects.get(pk=pk)
    # To check if the article is disliked and if true then to remove the dislike
    disliked = False
    for dislike in article.dislikes.all():
        if dislike == request.user:
            disliked = True
            break
    if disliked:
        article.dislikes.remove(request.user)

    # logic for like/unlike functionality
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

# dislike functionality
def dislikeView(request,pk,*args,**kwargs):
    article = Articles.objects.get(pk=pk)
    # To check if the article is disliked and if true then to remove the dislike
    liked = False
    
    for like in article.likes.all():
        if like == request.user:
            liked = True
            break
    
    if liked:
        article.likes.remove(request.user)

    # logic for dislike functionality
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

def blockView(request,pk,*args,**kwargs):
    article = Articles.objects.get(pk=pk)
    blocked = False
    for block in article.blocks.all():
        if block == request.user:
            blocked = True
            break
    if not blocked:
        article.blocks.add(request.user)
    if blocked:
        article.blocks.remove(request.user)
    next  = request.POST.get('next','/dashboard')
    return HttpResponseRedirect(next)

class UpdateCategoryPreference(UpdateView):
    model = Profile
    Form_class = UpdateCategoryPreferenceForm
    template_name = 'dashboard.html'

def landingpage(request):
    return render(request,'landingPage.html')








    

    


    

