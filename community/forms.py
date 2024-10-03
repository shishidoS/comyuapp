from django import forms
from .models import Post, Videos
from .models import UserProfile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['title', 'video_file', 'description', 'thumbnail']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'hometown', 'grade']
