from rest_framework import serializers
from .models import Content, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Content
        fields = '__all__'