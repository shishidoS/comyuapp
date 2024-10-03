from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Announcement, Post, UserProfile, Videos
from .forms import PostForm, VideoForm
from .forms import UserProfileForm
from .models import UserProfile
from .models import Videos

def productvideo(request):
    video_id = request.GET.get('video_id')
    video = get_object_or_404(Videos, id=video_id)
    return render(request, 'community/productvideo.html', {'video': video})

@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # 保存後、同じページにリダイレクト
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'community/user_profile.html', {'form': form})
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
    posts = Post.objects.all().values('user', 'image_url', 'description')
    posts_list = list(posts)
    return JsonResponse(posts_list, safe=False)

@login_required
def create_post(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        try:
            post = Post.objects.create(
                user=user,
                title=title,
                description=description,
                image=image
            )
            return JsonResponse({'success': True, 'message': '投稿が成功しました。'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': '不正なリクエストです。'})

def video_list(request):
    videos = Videos.objects.all().order_by('-id')  # 'created_at'がない場合は'id'などで並べ替え
    return render(request, 'community/videos.html', {'videos': videos})

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

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'community/login.html', {'form': form})
