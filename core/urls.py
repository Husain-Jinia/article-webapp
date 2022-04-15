"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from article import views as article_views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    # Article urls
    path('dashboard/',article_views.dashboard, name='dashboard'),
    path('articleDetail/<int:pk>',article_views.ArticleDetailView.as_view(), name='article-detail'),
    path('articleCreation/',article_views.ArticleCreation.as_view(), name='article-creation'),
    path('articleView/',article_views.viewArticle, name='article-view'),
    path('articleUpdate/<int:pk>',article_views.UpdateArticle.as_view(), name='article-updation'),
    path('articleDelete/<int:pk>',article_views.DeleteArticle.as_view(), name='article-deletion'),
    # like/dislike urls
    path('like/<int:pk>',article_views.likeView,name='like-article'),
    path('dislike/<int:pk>',article_views.dislikeView,name='dislike-article'),
    # user auth urls
    path('profile/',user_views.profile, name='profile'),
    path('register/',user_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
