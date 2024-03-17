import re
import hashlib
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def register(username, password):
    if not is_valid_username(username):
        return "Invalid Username: Please only use letters, numbers, and _"
    
    if User.objects.filter(username=username).exists():
        return "Username already exists"
    
    hashed_password = hash_password(password)
    new_user = User.objects.create_user(username=username, password=hashed_password)
    new_user.save()
    return "Registration successful"

def login(username, password):
    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        return True
    return False

def logout(request):
    request.session.flush()
    return "Logged out"

def is_valid_username(username):
    pattern = re.compile(r'^[\wäöüßÄÖÜ]+$')
    return bool(pattern.match(username))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def admin_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect('admin_login')
    else:
        form = UserCreationForm()
    return render(request, 'admin/register.html', {'form': form})
