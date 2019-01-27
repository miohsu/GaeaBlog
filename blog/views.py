from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Post, Tag, Category


# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'

