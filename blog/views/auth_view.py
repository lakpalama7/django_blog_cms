

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

def loginuser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user=user) #store user in session table and create session id
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'auth/login.html')