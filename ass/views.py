from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from ass.models import PostArticle
from .forms import CreateUser, PostForm, addQuestionform, QuesModel

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
        return redirect('home')
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


def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'ass/addQuestion.html',context)
    else: 
        return redirect('home')




def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1

        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'ass/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'ass/home.html',context)