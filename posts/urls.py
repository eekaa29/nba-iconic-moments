from django.urls import path
from .views import PostListView, UpdatePostView, SuccessView, PostDeleteView, PostCreateView

urlpatterns = [
    path("<int:pk>/", PostListView.as_view(), name="post_list"),
    path("create/<int:pk>", PostCreateView.as_view(), name="create_post"),
    path("update/<int:pk>/", UpdatePostView.as_view(), name="post_edit"),
    path("success/<int:pk>", SuccessView.as_view(), name="success"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete_post"),

]