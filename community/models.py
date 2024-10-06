# community/models.py
from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# models.py
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # null=Trueを追加
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}によるコメント"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # related_name を追加
    nickname = models.CharField(max_length=30, blank=True)
    hometown = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=10, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username
class Videos(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    completprogram = models.FileField(upload_to='programs/', blank=True, null=True)
    program_video = models.FileField(upload_to='videos/', blank=True, null=True)
    program_description = models.TextField(blank=True, null=True)  # プログラム動画の説明
    difficulty = models.PositiveIntegerField(choices=[
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ], default=1)

    def get_stars(self):
        return '★' * self.difficulty

    def __str__(self):
        return f"{self.title} - 難易度: {self.get_stars()}"