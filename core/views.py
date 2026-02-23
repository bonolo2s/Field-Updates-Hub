#from django.contrib.auth import models
from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import FieldUpdateForm, RegisterForm, FieldUpdate    
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import FieldUpdate
from django.db.models import Q
from django.core.paginator import Paginator

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            send_mail(
                subject="Welcome to Field Updates Hub!",
                message=f"Hi {user.first_name}, your account is ready.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            
            messages.success(request, "Account created! Check your email.")
            return redirect('login')
    
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            messages.error(request, "Invalid credentials.")
    
    return render(request, 'registration/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You've been logged out.")
        return redirect('/')
    return redirect('feed')

@login_required
def create_update(request):
    if request.method == 'POST':
        form = FieldUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = FieldUpdateForm()
    return render(request, 'core/create_update.html', {'form': form})

@login_required
def edit_update(request, pk):
    post = get_object_or_404(FieldUpdate, pk=pk)
    if not post.can_edit(request.user):
        return redirect('feed')
    if request.method == 'POST':
        form = FieldUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if request.POST.get('remove_image'):
                post.image.delete(save=False)
                post.image = None
            post.save()
            return redirect('feed')
    else:
        form = FieldUpdateForm(instance=post)
    return render(request, 'core/edit_update.html', {'form': form, 'post': post})

@login_required
def delete_update(request, pk):
    post = FieldUpdate.objects.get(pk=pk)
    if not post.can_edit(request.user):
        messages.error(request, "You can't delete this post.")
        return redirect('feed')
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Deleted!")
        return redirect('feed')
    return render(request, 'core/delete_update.html', {'post': post})

def landing(request):
    if request.user.is_authenticated:
        return redirect('feed')
    posts = FieldUpdate.objects.all().order_by('-created_at')[:3] 
    return render(request, 'landing.html', {'posts': posts})

@login_required
def feed(request):
    posts = FieldUpdate.objects.all().order_by('-created_at')
    return render(request, 'core/feed.html', {'posts': posts})

from django.contrib.auth.models import User

@login_required
def community(request):
    users = User.objects.all().annotate(post_count=models.Count('field_updates'))
    return render(request, 'core/community.html', {'users': users})

@login_required
def profile(request, pk):
    user = User.objects.get(pk=pk)
    posts = FieldUpdate.objects.filter(author=user).order_by('-created_at')
    return render(request, 'core/profile.html', {'profile_user': user, 'posts': posts})

def feed(request):
    posts = FieldUpdate.objects.all().order_by('-created_at')
    
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')
    
    
    if category:
        posts = posts.filter(category=category)

    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(message__icontains=search) |
            Q(author__first_name__icontains=search) |
            Q(author__last_name__icontains=search)
        )
    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'core/feed.html', {
        'posts': page_obj,
        'page_obj': page_obj,
        'total_posts': FieldUpdate.objects.count(),
        'total_members': User.objects.count(),
        'selected_category': category,
        'search': search,

    })

def profile_modal(request, pk):
    from django.contrib.auth.models import User
    profile_user = get_object_or_404(User, pk=pk)
    posts = FieldUpdate.objects.filter(author=profile_user).order_by('-created_at')
    return render(request, 'core/profile_modal.html', {
        'profile_user': profile_user,
        'posts': posts,
    })

