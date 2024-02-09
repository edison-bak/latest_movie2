from rest_framework import serializers

from movie_api.models import *

class movie_rankingSerializer(serializers.ModelSerializer):
    movieNm=serializers.CharField()
    rank=serializers.IntegerField()
    audiAcc=serializers.IntegerField()

    class Meta:
        model = movie_ranking
        fields = (
            "movieNm",
            "rank",
            "audiAcc",
        )