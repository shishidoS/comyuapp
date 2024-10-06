from django import forms
from .models import Post, Videos
from .models import UserProfile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']
class VideoForm(forms.ModelForm):
    DIFFICULTY_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]

    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES, label='難易度', required=True)

    class Meta:
        model = Videos
        fields = ['title', 'video_file', 'program_video', 'description', 'thumbnail', 'program_description', 'difficulty']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'hometown', 'grade', 'profile_image']