'''
1. `Case`: 데이터베이스에서 조건에 따라 다른 값을 반환하는 함수입니다. 예를 들어, 성별이 "남성"인 경우에는 "M", 그렇지 않은 경우에는 "F"를 반환할 수 있습니다.

2. `F`: 데이터베이스 필드의 값을 가져오고 업데이트하는데 사용되는 함수입니다. 다른 필드의 값을 가져와서 계산하거나 업데이트할 때 유용합니다.

3. `Sum`: 데이터베이스에서 특정 필드의 값을 모두 합산하는 함수입니다. 주로 그룹화된 쿼리나 특정 조건을 만족하는 레코드들의 값을 합산할 때 사용됩니다.

4. `Value`: 특정 값을 나타내는 객체를 생성하는 함수입니다. 이 객체는 데이터베이스 쿼리에서 특정 값을 지정할 때 사용됩니다.

5. `When`: Case 문에서 각 조건에 대한 조건절을 지정하는 함수입니다. Case 문에서 사용되며, 각 조건에 대한 조건식과 그에 해당하는 값을 지정합니다.
'''
from django.db.models import Case, F, Sum, Value, When
# Coalesce 함수는 여러 개의 인자 중에서 첫 번째로 NULL이 아닌 값을 반환하는 함수
from django.db.models.functions import Coalesce

# RESTful API를 만들기 위한 일반적인 클래스 기반 뷰를 제공
'''ListAPIView: 리스트 형식의 리소스를 나타내는 뷰를 제공합니다. 이 뷰를 사용하면 데이터베이스 쿼리 결과를 시리얼라이저를 통해 JSON 형식으로 반환할 수 있습니다.

RetrieveAPIView: 단일 리소스를 나타내는 뷰를 제공합니다. 이 뷰를 사용하여 데이터베이스에서 단일 객체를 가져와 JSON 형식으로 반환할 수 있습니다.

CreateAPIView: 새로운 리소스를 생성하는 뷰를 제공합니다. 이 뷰를 사용하여 POST 요청을 통해 새로운 객체를 생성하고 데이터베이스에 저장할 수 있습니다.

UpdateAPIView: 기존의 리소스를 업데이트하는 뷰를 제공합니다. 이 뷰를 사용하여 PUT 또는 PATCH 요청을 통해 객체를 업데이트할 수 있습니다.

DestroyAPIView: 기존의 리소스를 삭제하는 뷰를 제공합니다. 이 뷰를 사용하여 DELETE 요청을 통해 객체를 삭제할 수 있습니다.

ListCreateAPIView: 리스트 및 생성 기능을 모두 제공하는 뷰를 제공합니다. 이 뷰를 사용하여 리스트 조회와 새로운 객체 생성 기능을 한 번에 제공할 수 있습니다.'''
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
# Response 클래스를 사용하여 데이터를 포함한 응답을 생성하였습니다. 이 응답은 클라이언트에게 JSON 형식으로 반환
from rest_framework.response import Response
from rest_framework.views import APIView

from movie_api.models import movie_ranking
# from movie_api.pagination import PostPageNumberPagination
from .serializers import movie_rankingSerializer

class movieRanking(generics.ListCreateAPIView):
    serializer_class = movie_rankingSerializer

    def get_queryset(self):
        # id를 기준으로 정렬된 queryset을 반환합니다.
        out = movie_ranking.objects.all().order_by('rank')
        return out