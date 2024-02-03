from django.contrib import admin
from .models import Content, Author


admin.site.register(Author)
admin.site.register(Content)
