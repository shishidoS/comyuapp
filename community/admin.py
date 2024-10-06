#admin.py
from django.contrib import admin
from .models import Post, Videos
from .models import UserProfile

admin.site.register(Post)
admin.site.register(Videos)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'hometown', 'grade', 'profile_image']