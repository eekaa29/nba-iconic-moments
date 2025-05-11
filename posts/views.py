from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from franchise.models import Franchise
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name="posts/post_list.html"

    def get_queryset(self):
        franchise_id = self.kwargs['pk']
        return Post.objects.filter(franchise_id=franchise_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['franchise'] = Franchise.objects.get(pk=self.kwargs['pk'])
        return context

