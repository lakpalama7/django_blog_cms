

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(
            email = email,
            username = username,
        )
        user.set_password(password) #hashing password
        user.save()
        return redirect('login')

        
    return render(request, 'auth/register.html')

def login(request):
    return render(request, 'auth/login.html')