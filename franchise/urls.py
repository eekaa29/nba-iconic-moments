from django.urls import path
from .views import ConferenceChoice, FranchiseListView

urlpatterns = [
    path("", ConferenceChoice.as_view(), name = "conference_list"),
    path("<slug:conference>/", FranchiseListView.as_view(), name = "franchise_list"),
]