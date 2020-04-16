from django.shortcuts import render, redirect, resolve_url, reverse
from django.contrib import messages
from .models import Message, Comment, User

# Create your views here.
def index(request):
    if request.session['id']:
        context = {
            'posts': Message.objects.all()
        }
        return render(request, 'wall_app/index.html', context)
    return redirect(reverse('login:index'))

def new(request):
    if request.session['id']:
        return render(request, 'wall_app/new.html')
    return redirect(reverse('login:index'))

def create(request):
    if request.session['id']:
        if request.method == "POST":
            Message.objects.create(message = request.POST['post'])
            return redirect('wall:index')
    return redirect(reverse('login:index'))

def edit(request, post_id):
    if request.session['id']:        
        message = Message.objects.get(id=post_id)
        context = {'message': message}
        return render(request, "wall_app/edit.html", context)
    return redirect(reverse('login:index'))

def update(request, post_id):
    if request.session['id']:
        if request.method == "POST":
            message = Message.objects.get(id = post_id)
            message.message = request.POST['post']
            message.save()
            return redirect('wall:index')
    return redirect(reverse('login:index'))

def destroy(request, post_id):
    if request.session['id']:
        if request.method == "POST":
            message = Message.objects.get(id = post_id)
            message.delete()
            return redirect('wall:index')
    return redirect(reverse('login:index'))

def new_like(request, move_id):
    if request.session['id']:
        if request.method == "POST":
            message = Message.objects.get(id = post_id)
            user = User.objects.get(id= request.session['id'])
            message.like.add(user)
            return redirect(reverse('wall:index'))
    return redirect(reverse('login:index'))

def show(request):
    if request.session['id']:
        users = User.objects.all()
        context = {'users': users}
        return render(request, "wall_app/show.html", context)
    return redirect(reverse('login:index'))

def new_follow(request, user_id):
    if request.session['id']:
        if request.method == "POST":
            followed = User.objects.get(id = user_id)
            user = User.objects.get(id= request.session['id'])
            followed.follow.add(user)
            return redirect(reverse('wall:index'))
    return redirect(reverse('login:index'))