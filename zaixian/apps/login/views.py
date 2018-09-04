# from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from .models import UserA
from django.http import HttpResponse
# Create your views here.
def login(request):
   pass
   # if
   # return render(request,'login.html')
def zhuce(request):
   context={}
   email = request.POST.get("email")
   passwd = request.POST.get("passwd")
   all_list = UserA.objects.all()
   for i in all_list:
      # if i.email==email:
      #    context["info"] = "该邮箱已注册！！"
      #    return render(request,'register.html',context)
      if i.email != email:
         user = UserA()
         user.objects.create(email=email, passwd=passwd)
         #
         # user.create(email,passwd)
         # info="注册成功！！！！"
         return HttpResponse(email, passwd)
      # return HttpResponse(email, passwd)
      # return redirect(reverse("login:login"))
      else:
         #    # return HttpResponse("asdasdasd")
         context["info"] = "该邮箱已注册！！"
         return render(request, 'register.html', context)
def register(request):
   # if request.method=="POST":
   #    context={}
   #    email=request.POST.get("email")
   #    passwd = request.POST.get("passwd")
   #    # if User.objects.get(email=email).count:
   #    all_list = UserA.objects.all()
   #    for i in all_list:
   #       # if i.email==email:
   #       #    context["info"] = "该邮箱已注册！！"
   #       #    return render(request,'register.html',context)
   #       if i.email != email:
   #          user = UserA()
   #          user.objects.create(email=email,passwd=passwd)
   #          #
   #          # user.create(email,passwd)
   #          # info="注册成功！！！！"
   #          return HttpResponse(email,passwd)
   #       # return HttpResponse(email, passwd)
   #          # return redirect(reverse("login:login"))
   #       else:
   #       #    # return HttpResponse("asdasdasd")
   #          context["info"]="该邮箱已注册！！"
   #          return render(request,'register.html',context)
   #
   # else:
      return render(request,'register.html')

