#viviapp/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from community.views import user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('community/', include('community.urls')),
     path('user_profile/', user_profile, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
