from django.urls import path
from .views import PostDetailView, PostListView

urlpatterns = [
    path("<int:pk>/", PostListView.as_view(), name="post_list"),
]