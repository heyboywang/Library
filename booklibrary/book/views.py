from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SuserForm
# Create your views here.

def index(request):
    username = request.session.get("username")
    if username:
        return render(request, "booklibrary/index.html",{"username":username})
    else:
        return render(request,"booklibrary/index.html")
    # return HttpResponse("shouye")

def user_login(request):
    # form = SLoginForm()
    # context = {
    #     "form": form
    # }
    return render(request,"booklibrary/user_login.html")

def user(request):
    return render(request, "booklibrary/user.html")

def login_tools(request):
    users = Suser.objects.all()
    # form = SLoginForm(request.POST)

    for user in users:
        if user.username == request.POST["username"]:
            if user.password == request.POST['pwd']:
                request.session["username"] = user.username
                return render(request,"booklibrary/user.html",{"user":user})

                # return HttpResponse("登录成功")
        else:
            return render(request, "booklibrary/index.html")

def logout(request):
    request.session.clear()
    return render(request, "booklibrary/index.html")

def user_register(request):
    form = SuserForm()
    context = {
        "form":form
    }
    return render(request, "booklibrary/user_register.html",context)

def register_tools(request):
    form = SuserForm(request.POST)
    form.save()
    return render(request, "booklibrary/user_login.html")

def user_info(request):
    pass