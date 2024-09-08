#admin.py
from django.contrib import admin
from .models import Post, Videos

admin.site.register(Post)
admin.site.register(Videos)