from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


# Class-based view for index.html
class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


# Class-based view for post details
class PostDetailView(DetailView):
    model = Post


# Class-based view for creating a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Class-based view for updating a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# About page view with info about the app
def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'posts/about.html', context)
