from django.db import models

from django.db import models

from content.managers import ContentManager


class Author(models.Model):
    unique_id = models.IntegerField(unique=True, db_index=True)

    username = models.CharField(max_length=255)
    # Using JSON field for rest of data just for faster coding in Hackathon.
    # We should write fields for each data field
    data = models.JSONField(blank=True, null=True)  # blank allowed only for faster implementation

    def __str__(self):
        return f"{self.username}"


class Content(models.Model):
    unique_id = models.IntegerField(unique=True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Using JSON field for rest of data just for faster coding in Hackathon.
    # We should write fields for each data field
    data = models.JSONField(blank=True, null=True)  # blank allowed only for faster code

    objects = ContentManager()
