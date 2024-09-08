#community/views.pyです
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Announcement, Post, UserProfile
from .forms import PostForm
from django.http import JsonResponse
from .models import Post, Videos
from django.shortcuts import render, redirect
from .models import Post, Videos  # Videoモデルをインポート
from .forms import PostForm, VideoForm  # VideoFormをインポート
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'community/signup.html', {'form': form})

@login_required
def home(request):
    announcements = Announcement.objects.order_by('-created_at')[:5]
    posts = Post.objects.all()
    return render(request, 'community/home.html', {'announcements': announcements, 'posts': posts})


@login_required
def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'community/user_profile.html', {'profile': profile})

def hiroba(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community/hiroba.html', {'posts': posts})

def upload(request):
    # ここにファイルアップロード処理を実装
    return render(request, 'community/upload.html')
def get_posts(request):
    posts = list(Post.objects.values('user', 'image_url', 'description'))
    return JsonResponse(posts, safe=False)

def get_posts(request):
    posts = Post.objects.all().values('user', 'image_url', 'description')
    posts_list = list(posts)
    return JsonResponse(posts_list, safe=False)

@login_required
def create_post(request):
    print('Received request method:', request.method)  # デバッグ用

    if request.method == 'POST':
        user = request.POST.get('user')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        print('Received data:', user, title, description, image)  # デバッグ用

        try:
            post = Post.objects.create(
                user=user,
                title=title,
                description=description,
                image=image
            )
            return JsonResponse({'success': True, 'message': '投稿が成功しました。'})
        except Exception as e:
            print('Error:', str(e))  # デバッグ用
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': '不正なリクエストです。'})
def video_list(request):
    videos = Videos.objects.all().order_by('-created_at')
    return render(request, 'community/video_list.html', {'videos': videos})

def post_list(request):
    posts = Post.objects.all()  # 例として全てのポストを取得
    return render(request, 'community/post_list.html', {'posts': posts})
@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'community/upload.html', {'form': form})