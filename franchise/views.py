from django.shortcuts import render
from .models import Franchise
from django.views.generic.list import ListView
# Create your views here.

class FranchiseListView(ListView):
    model = Franchise
    template_name = "franchise/franchise_list.html"


