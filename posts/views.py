from django.shortcuts import render
# from django.http import HttpResponse

from .models import Post

# Create your views here.


# Home page view with blog posts
def index(request):
    context = {
        'title': 'Latest Posts',
        'posts': Post.objects.all()[:10]
    }

    return render(request, 'posts/index.html', context)


# About page view with info about the app
def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'posts/about.html', context)


# Details page view with info about a certain post
def details(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)
