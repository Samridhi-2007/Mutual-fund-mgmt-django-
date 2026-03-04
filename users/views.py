from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from advisors.models import Advisor
from education.models import Article
from funds.models import Fund
from .forms import ProfileUpdateForm

User = get_user_model()
PUBLIC_ROLES = {'INVESTOR', 'ADVISOR'}


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        role = request.POST.get('role', '').strip().upper()

        if not username or not email or not password or role not in PUBLIC_ROLES:
            messages.error(request, 'Please fill all fields with valid values.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        User.objects.create_user(username=username, email=email, password=password, role=role)
        messages.success(request, 'Registration successful. Please log in to continue.')
        return redirect('login')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

        login(request, user)
        return redirect('dashboard')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        'fund_count': Fund.objects.count(),
        'article_count': Article.objects.count(),
        'advisor_count': Advisor.objects.count(),
    }
    return render(request, 'users/dashboard.html', context)


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'users/profile_edit.html', {'form': form})
