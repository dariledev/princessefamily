from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from ass.models import PostArticle
from .forms import CreateUser, PostForm

# Create your views here.



def index(request):
    return render(request, 'ass/index.html')



def detail(request):
    return render(request, 'ass/detail.html')

def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    return render(request, 'ass/login.html')


def register(request):
    forms = CreateUser()
    if request.method == 'POST':
        forms = CreateUser(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    return render(request, 'ass/register.html', {'forms':forms})


def payement(request):
    return render(request, 'ass/payement.html')


def donateur(request):
    return render(request, 'ass/donateur.html')


def projets(request):
    post = PostArticle.objects.all()
    return render(request, 'ass/projets.html', {'post':post})

def projets_don(request):

    return render(request, 'ass/projetsdon.html')

def celibat(request):
    return render(request, 'ass/celibat.html')


def error(request):
    return render(request, 'ass/error.html')

def add(request):
    postform = PostForm()
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            postform.save()
            return redirect('projets')
    return render(request, 'ass/add.html', {'postform':postform})