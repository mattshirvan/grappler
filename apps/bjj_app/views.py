from django.shortcuts import render, redirect, reverse
from apps.login_app.models import User
from apps.bjj_app.models import Move    
from django.contrib import messages



# Create your views here.
def index(request):
    if not request.session['id']:
        return redirect(reverse('login:index'))
    moves = Move.objects.all()
    print(moves)
    context = {'moves': moves}
    return render(request, "bjj_app/index.html", context)

def create(request):
    if request.session['id']:
        if request.method == "POST": 
            user = User.objects.get(id=request.session['id'])           
            Move.objects.create(name = request.POST['name'], description = request.POST['description'], creator = request.POST['creator'], user = user)
    return redirect(reverse('bjj:index'))

def show(request):
    if request.session['id']:
        user = User.objects.get(id=request.session['id'])
        moves = Move.objects.filter(user = user)
        context = {'moves': moves}
        return render(request, 'bjj_app/show.html', context)
    return redirect(reverse('login:index'))

def edit(request, move_id):
    if request.session['id']:
        move = Move.objects.get(id = move_id)
        context = {'move': move}
        return render(request, "bjj_app/edit.html", context)        
    return redirect(reverse('login:index'))

def update(request, move_id):
    if request.session['id']:
        if request.method == "POST":        
            move = Move.objects.get(id = move_id)
            move.name = request.POST['name']
            move.description = request.POST['description']
            move.creator = request.POST['creator']
            move.save()
            return redirect(reverse('bjj:index'))
    return redirect(reverse('login:index'))

def destroy(request, move_id):
    if request.session['id']:
        if request.method == "POST":        
            move = Move.objects.get(id = move_id)
            move.delete()
            return redirect(reverse('bjj:index'))
    return redirect(reverse('login:index'))

def new(request, move_id):
    if request.session['id']:
        if request.method == "POST":
            user = User.objects.get(id = request.session['id'])
            move = Move.objects.get(id=move_id)
            move.like.add(user)
            return redirect(reverse('bjj:index'))
    return redirect(reverse('login:index'))

def new_search(request):
    if request.session['id']:    
        return render(request, "bjj_app/search.html")
    return redirect(reverse('login:index'))

def move_api(request):
    if request.session['id']:
        move = Move.objects.filter(name=request.POST['starts_with'])
        context = {'move': move}
        return render(request,'bjj_app/search.html', context)
    return redirect(reverse('login:index'))