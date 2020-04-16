from django.shortcuts import render, redirect, reverse
from .models import User
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def new(request):
    return render(request, 'login_app/new.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
            print(errors)
            return redirect(reverse("login:index"))
    
    hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    print(hash)
    user = User.objects.create(name = request.POST['name'], username = request.POST['username'], email = request.POST['email'], hash = hash.decode())
    print(user)
    return redirect(reverse('login:index'))

def show(request):
    print(request.POST['username'])
    user = User.objects.filter(username=request.POST['username'])
    print(user)
    if not bcrypt.checkpw(request.POST['password'].encode(), user[0].hash.encode()):
        return redirect(reverse('login:index'))
    else:
        request.session['user'] = user[0].username
        request.session['id'] = user[0].id
        return redirect(reverse('bjj:index'))

def destroy(request):
    request.session.clear()
    return redirect('login:index')