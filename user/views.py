from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from hashlib import sha256
from .models import User

def login(request):
    status = request.GET.get('status')
    return render(request,'login.html', {'status': status})
    

def login_validation(request):

    sub_user_email = request.POST.get('user_email')
    sub_user_password = request.POST.get('user_password')
    sub_user_password = sha256(sub_user_password.encode()).hexdigest()

    user_login = User.objects.filter(user_email = sub_user_email).filter(user_password=sub_user_password)

    if len(user_login)==0:
        return redirect('/auth/login?status=1')
    elif len(user_login)==1:
        request.session['user'] = user_login[0].id
        return redirect(f'/book/home?user_id={request.session['user']}')

def logout(request):
    request.session.flush()
    return redirect('/auth/login')
    

def register(request):
    status = request.GET.get('status')
    return render(request,'register.html', {'status': status})


def user_register_validation(request):
    sub_username = request.POST.get('user_name')
    sub_useremail = request.POST.get('user_email')
    subu_serpassword = request.POST.get('user_password')

    new_user = User.objects.filter(user_name = sub_username)
    new_mail = User.objects.filter(user_email = sub_useremail)

    if len(sub_username.strip()) == 0 or len(sub_useremail.strip()) == 0:
        return redirect('/auth/register?status=1')


    if len(subu_serpassword)< 6:
        return redirect('/auth/register?status=2')

    
    if len(new_user)>0 or len(new_mail)>0:
        return redirect('/auth/register?status=3')
  

    try:
        newuserpassword = sha256(subu_serpassword.encode()).hexdigest()
        user = User(user_name=sub_username,
                    user_email=sub_useremail,
                    user_password=newuserpassword)
        user.save()
        return redirect('/auth/register?status=0')

    except Exception as e:
        print(e)
        return redirect('/auth/register?status=4')
    
    