from django.urls import path
from .views import PostsView

urlpatterns = [
    path('posts/', PostsView),
    path('posts/<int:pk>/', PostsView),
]