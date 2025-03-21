from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def cadastrar(request):
    return HttpResponse('Hellow world')

def home(request):
    if request.session.get('user'):
        return HttpResponse('home')
    else:
        return redirect('/auth/login?status=2')