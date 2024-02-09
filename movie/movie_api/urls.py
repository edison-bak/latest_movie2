from django.urls import path

from .views import *

urlpatterns = [
    path("movie_ranking/", movieRanking.as_view(), name="movieRanking"),
]