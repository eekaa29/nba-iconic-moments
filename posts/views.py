from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView, DeleteView, CreateView
from franchise.models import Franchise
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UpdateViewForm, CreateViewForm
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

@method_decorator(staff_member_required, name="dispatch")
class PostCreateView(CreateView):
    model=Post
    template_name = "posts/create_form.html"
    form_class = CreateViewForm
    def get_success_url(self):
        return reverse_lazy("post_list", args=[self.object.franchise.pk])

@method_decorator(staff_member_required, name="dispatch")
class UpdatePostView(UpdateView):
    model= Post
    form_class = UpdateViewForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy("success", args=[self.object.franchise.pk])

@method_decorator(staff_member_required, name="dispatch")
class PostDeleteView(DeleteView):
    model= Post
    template_name_suffix = "_confirm_delete"
    def get_success_url(self):
        return reverse_lazy("post_list", args=[self.object.franchise.pk])
    
class SuccessView(TemplateView):
    template_name = "posts/success_view.html"
    
