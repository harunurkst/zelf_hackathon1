from django.db import models

from django.db import models


class Author(models.Model):
    unique_id = models.IntegerField()

    username = models.CharField(max_length=255)

    data = models.JSONField(blank=True, null=True)  # blank allowed only for faster implementation

    def __str__(self):
        return f"{self.username}"


class Content(models.Model):
    unique_id = models.IntegerField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    data = models.JSONField(blank=True, null=True)  # blank allowed only for faster code
