from django.db import models

class movie_ranking(models.Model):
    movieNm=models.CharField(max_length=20, unique=True)
    rank=models.IntegerField(default=100)
    audiAcc=models.IntegerField(default=0)