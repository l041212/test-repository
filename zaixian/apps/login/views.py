# from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse
from apps.utils.commons import *
from apps.login.models import *
from django.db import connection
import pymysql
# Create your views here.my

def login(request):
   context={}
   return render(request,'login.html',context)

def login_handler(request):
    code = request.POST.get('code')
    password = request.POST.get('password')
    users = User.objects.filter(code=code,password=password)#账户密码要一致
    if len(users) > 0:
        request.session["user_id"] = users[0].id
        return redirect("/jobInfo/list/")
    else:

        return redirect("/login/login/")

def register(request):
        context={}
        return render(request, 'register.html', context)

@mirror(User())
def register_handler(request, entity):
    code = request.POST.get('code')
    users = User.objects.filter(code=code)
    if len(users) >0:
         return HttpResponse('账户已经注册')


    else:
        User.save(entity)
        return redirect('/login/login')
