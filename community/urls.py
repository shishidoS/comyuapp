#community/urls.py
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import get_posts
from .views import create_post

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('create_post/', views.create_post, name='create_post'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('hiroba/', views.hiroba, name='hiroba'),
    path('upload/', views.upload, name='upload'),
    path('videos/', views.video_list, name='video_list'),  # ここがvideo_listになっている
    path('posts/', views.post_list, name='post_list'),
    path('video/', views.productvideo, name='productvideo'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('get_posts/', views.get_posts, name='get_posts'),
    path('login/', views.login_view, name='login'),
]
