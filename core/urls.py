from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_update, name='create_update'),
    path('edit/<int:pk>/', views.edit_update, name='edit_update'),
    path('delete/<int:pk>/', views.delete_update, name='delete_update'),
    path('', views.landing, name='landing'),
    path('feed/', views.feed, name='feed'),
    path('community/', views.community, name='community'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile-modal/<int:pk>/', views.profile_modal, name='profile_modal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)