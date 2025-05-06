from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name="posts/post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
