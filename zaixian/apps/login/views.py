# from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from .models import User
from django.http import HttpResponse
from apps.utils.commons import *
# Create your views here.my
def login(request):

   context={}
   return render(request,'register.html',context)
   #request.session["user_id"] = xxx

def login_handler(request):

   email = request.POST.get("email")
   password = request.POST.get("password")
   isChecked=request.POST.get('is_checked')
 
def register(request):
      context={}
      return render(request, 'register.html', context)

@mirror(User())
def register_handler(request, entity):
      User.save(entity)
      return redirect('/login/login')

# # if request.method=="POST":
#    #    context={}
#
#       '''
#       email=request.POST.get("email")
#       password = request.POST.get("password")
#       user = User()
#       user.email(email)
#       user.password(password)
#       User.save(user)
#       print(email)
#       print(password)
#       print(entity.name)
#       print(entity.code)
#       print(entity.role)
#       '''


