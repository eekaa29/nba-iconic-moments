from django.urls import path
from .views import get_latest_articles

urlpatterns = [
    path("show/", get_latest_articles, name="latest_articles"),
]