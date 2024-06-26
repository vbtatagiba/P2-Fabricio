from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import MyObject
from .forms import MyObjectForm

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def object_list(request):
    objects = MyObject.objects.filter(created_by=request.user)
    return render(request, 'object_list.html', {'objects': objects})

@login_required
def object_create(request):
    if request.method == 'POST':
        form = MyObjectForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect('object_list')
    else:
        form = MyObjectForm()
    return render(request, 'object_form.html', {'form': form})

@login_required
def object_edit(request, id):
    obj = get_object_or_404(MyObject, id=id, created_by=request.user)
    if request.method == 'POST':
        form = MyObjectForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('object_list')
    else:
        form = MyObjectForm(instance=obj)
    return render(request, 'object_form.html', {'form': form})

@login_required
def object_delete(request, id):
    obj = get_object_or_404(MyObject, id=id, created_by=request.user)
    if request.method == 'POST':
        obj.delete()
        return redirect('object_list')
    return render(request, 'object_confirm_delete.html', {'object': obj})

@login_required
def chat_view(request):
    return render(request, 'chat.html')

