from django.shortcuts import render
from django.views.generic import ListView

from .models import Post, Tag, Category


# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    paginate_by = 5

