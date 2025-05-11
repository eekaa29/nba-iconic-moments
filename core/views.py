from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "core/home.html"

class AboutView(TemplateView):
    template_name="core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rango"]= range(7)
        return context

class ContactView(TemplateView):
    template_name = "core/contact.html"

