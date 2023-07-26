from django.urls import path
from .views import MovieListView,MovieDetailView,PostListView,PostDetailView

urlpatterns = [
    path('',MovieListView.as_view(), name = 'movie_list'),
    path('<int:pk>/',MovieDetailView.as_view(), name= 'moive_detail'),

    path('post/', PostListView.as_view(), name= 'post_list'),
    path('post/<int:pk>/',PostDetailView.as_view(), name= 'post_detail'),


]
