from django.shortcuts import render,redirect,reverse
from .models import User
from django.http import HttpResponse
from apps.utils.commons import *
from apps.login.services import *
import json
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

def info(request):
    return render(request, "login_info.html")

@mirror(User())
def signin(request, entity):
    users = getUserByCodeAndPassword(entity.code, entity.password)
    if(users != None and len(users)==1):
        request.session["user_id"] = users[0].id
        return redirect("/jobInfo/list/")
    return redirect("/login/info/")

def signout(request):
    request.session.flush()
    return redirect("/login/info/")

@mirror(User())
def save(request, entity):
      flag = saveUser(request, entity)
      return HttpResponse(flag)

def unTester(request):
    users = getUserByRole('test')
    return HttpResponse(json.dumps(opposite(users)), content_type='application/json')
