from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User

# Create your views here.


def cadastrar(request):
    return HttpResponse('Hellow world')

def home(request):
    if request.session.get('user'):
        user_login = User.objects.get(id=request.session['user']).user_name
        return HttpResponse(f'Hello {user_login}')
    else:
        return redirect('/auth/login?status=2')