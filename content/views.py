from django.db.models.fields.json import KeyTextTransform
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Sum, Avg
from .models import Content
from .serializers import ContentSerializer


class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentSingleView(generics.RetrieveDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'unique_id'


class StatisticsView(APIView):
    def get(self, request):
        content = Content.objects.all()
        likes = Content.objects.annotate(val=KeyTextTransform('data', 'data__stats__digg_counts__likes__count')).aggregate(Sum('val'))
        print("likes", likes)
        data = {
            'total_content': content.count(),
            'likes': likes
        }
        return Response(data, status=status.HTTP_200_OK)