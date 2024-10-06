from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from .models import Announcement, Post, UserProfile, Videos
from .forms import PostForm, VideoForm, UserProfileForm

def productvideo(request):
    video_id = request.GET.get('video_id')
    video = get_object_or_404(Videos, id=video_id)
    return render(request, 'community/productvideo.html', {'video': video})

@login_required
@login_required  # ログインしているユーザーだけがアクセスできるようにする
def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        user = request.user  # ログインしているユーザー

        # Post モデルに新しい投稿を作成
        try:
            post = Post.objects.create(
                user=user,
                title=title,
                description=description,
                image=image
            )
            return redirect('hiroba')  # 成功後、hirobaページにリダイレクト
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return render(request, 'community/upload.html')  # GETリクエストの場合

def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
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
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # 現在ログインしているユーザーをセット
            post.save()
            return redirect('hiroba')  # 'hiroba' は hiroba.html に対応する URL 名
        else:
            return JsonResponse({'success': False, 'message': 'フォームが無効です。'})

    # GETリクエストの場合は、空のフォームを表示
    else:
        form = PostForm()

    return render(request, 'community/upload.html', {'form': form})

@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # プロフィールページにリダイレクト
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'community/user_profile.html', {'form': form})

def hiroba(request):
    posts = Post.objects.all().order_by('-created_at')  # 投稿を最新順に取得
    return render(request, 'community/hiroba.html', {'posts': posts})

def get_posts(request):
    posts = Post.objects.all().values('user', 'image', 'description')
    posts_list = list(posts)
    return JsonResponse(posts_list, safe=False)


def video_list(request):
    videos = Videos.objects.all().order_by('-id')  # 'created_at'がない場合は'id'などで並べ替え

    # 難易度に応じた★の文字列を生成
    for video in videos:
        video.stars = '★' * video.difficulty  # 難易度に応じた★の文字列を生成

    return render(request, 'community/videos.html', {'videos': videos})
def post_list(request):
    # ユーザーとそのプロフィールを一緒に取得
    posts = Post.objects.select_related('user__profile').all()
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

def videos(request):
    return render(request, 'community/videos.html')