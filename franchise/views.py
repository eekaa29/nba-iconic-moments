from django.shortcuts import render
from .models import Franchise
from django.views.generic.list import ListView
from django.views.generic import TemplateView
# Create your views here.

class ConferenceChoice(TemplateView):
    template_name = "franchise/conference_list.html"


class FranchiseListView(ListView):
    model= Franchise
    template_name = "franchise/franchise_list.html"

    def get_queryset(self):
        conference = self.kwargs["conference"]
        return Franchise.objects.filter(conference=conference)


    


