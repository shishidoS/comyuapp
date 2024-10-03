# community/models.py
from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photos/', default='photos/default.jpg')  # デフォルトの画像パスを設定
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True) 


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}によるコメント"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, blank=True)
    product_id = models.CharField(max_length=30, unique=True,default="default_id")
    hometown = models.CharField(max_length=50, blank=True)
    grade = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nickname or self.user.username
    
class Videos(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    completprogram = models.FileField(upload_to='programs/', blank=True, null=True)

    def __str__(self):
        return self.title