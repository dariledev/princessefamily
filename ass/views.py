from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'ass/index.html')



def detail(request):
    return render(request, 'ass/detail.html')



def register(request):
    return render(request, 'ass/register.html')


def donateur(request):
    return render(request, 'ass/donateur.html')