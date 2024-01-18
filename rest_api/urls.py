from django.urls import path
from .views import PostsView, Posts_detail

urlpatterns = [
    path('posts/', PostsView),
    path('details/<int:pk>/', Posts_detail),
]