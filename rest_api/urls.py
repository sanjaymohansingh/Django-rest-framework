from django.urls import path, include
from .views import PostsView
from rest_framework import routers

router = routers.SimpleRouter()

router.register('posts', PostsView, basename='posts')


urlpatterns = [
    # path('posts/', PostsView),
    # path('details/<int:pk>/', Posts_detail),

    # using class based views
    # path('posts/', PostsView.as_view()),
    # path('details/<int:pk>/', Posts_detail.as_view()),

    # using generic class based views
    # path('posts/<int:id>/', PostsView.as_view()),
   
   # using APIView
    path('', include(router.urls))
    
]