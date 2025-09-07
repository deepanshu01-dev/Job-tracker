from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def signup_view(request):
  if request.method == 'POST':
    username = request.POST.get('username').lower()
    # email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if password1 != password2:
       return render(request, 'accounts/register.html', {'error': 'passwords do not match!'})

    if User.objects.filter(username=username).exists():
       return render(request, 'accounts/register.html', {'error': 'Username already exists!'})
    try:
      user = User.objects.create_user(username=username, password=password1)
      user.save()
      return redirect('login')
    except IntegrityError: 
      return render(request, 'accounts/register.html', {'error': 'Failed to create user. Please try again.'})

  return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('job_list')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })
    return render(request, 'accounts/login.html')


def logout_view(request):
  logout(request)
  return redirect('home')

def delete_account(request):
  pass