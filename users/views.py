from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .forms import UserCreationForm, UserLoginForm

MyUser = get_user_model()

# Create your views here.
def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} Account created')
            return redirect('login')
    form = UserCreationForm()
    return render(request, 'users/register.html',{'form':form})


def login_user(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        query = form.cleaned_data.get('query')
        user = MyUser.objects.filter(
            Q(username=query) | 
            Q(email=query)
        ).distinct().first()
        login(request, user)
        return redirect('home')
    return render(request,'users/login.html',{'form':form})


def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect('login')


class AllUsers(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = MyUser
    template_name = 'users/home.html'
    context_object_name = 'users'