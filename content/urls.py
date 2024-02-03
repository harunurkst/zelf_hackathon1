from django.urls import path

from content.views import ContentListView, ContentSingleView, StatisticsView

urlpatterns = [
    path('content', ContentListView.as_view()),
    path('content/<int:unique_id>', ContentSingleView.as_view()),
    path('statistics', StatisticsView.as_view()),
]