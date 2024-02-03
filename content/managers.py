from django.db import models
from django.db.models import Sum, Avg
from utils.custom import NestableKeyTextTransform


class ContentManager(models.Manager):
    def total_likes(self):
        return self.get_queryset().annotate(val=NestableKeyTextTransform(
            'data', 'stats', 'digg_counts', 'likes', 'count')
        ).aggregate(Sum('val'))['val__sum']

    def total_views(self):
        return self.get_queryset().annotate(val=NestableKeyTextTransform(
            'data', 'stats', 'digg_counts', 'views', 'count')
        ).aggregate(Sum('val'))['val__sum']