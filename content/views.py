from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Content
from .serializers import ContentSerializer


class ContentListView(generics.ListAPIView):
    """
    API view to list all content with detail of Author
    url: /api/v1/content
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentSingleView(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete particular content
    url: /api/v1/content/<unique_id>
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'unique_id'


class StatisticsView(APIView):
    """
    API view to show statistics
    data format: {
            'total_content': <int>,
            'total_likes': <int>,
            'total_views': <int>
        }
    """
    def get(self, request):
        content = Content.objects.all()
        likes = Content.objects.total_likes()
        views = Content.objects.total_views()
        data = {
            'total_content': content.count(),
            'total_likes': likes,
            'total_views': views
        }
        return Response(data, status=status.HTTP_200_OK)