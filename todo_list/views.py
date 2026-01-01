from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Todoo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def index(request):
    if request.method == "POST":
        username = request.POST.get("fnn")
        email = request.POST.get("email")
        password = request.POST.get("pwd")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "signup.html")

        User.objects.create_user(username=username, email=email, password=password)
        return redirect("/login")

    return render(request, "signup.html")


def login_page(request):
    if request.method == 'POST':
        fnn = request.POST.get('fnn')
        pwd = request.POST.get('pwd')
        print(fnn, pwd)

        user = authenticate(request, username=fnn, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/todopage')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/login')

    return render(request, "login.html")

@login_required
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todoo.objects.create(title=title, user=request.user)
        return redirect('/todopage')

    
    tasks = Todoo.objects.filter(user=request.user).order_by('-date')
    tasks_with_sr = [(i+1, task) for i, task in enumerate(tasks)]

    return render(request, 'todo.html', {'res': tasks_with_sr})


def edit_todo(request, id):
    task = Todoo.objects.get(srno=id, user=request.user)

    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            task.title = title   
            task.save()
        return redirect('/todopage')

    return render(request, "edit.html", {"task": task})


def delete_todo(request, srno):
    task = Todoo.objects.get(srno=srno)
    task.delete()
    return redirect('/todopage/')

def user_logout(request):
    logout(request)
    return redirect('login')
