from django.shortcuts import render,get_object_or_404,reverse
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SuserForm
from datetime import *
# Create your views here.

def index(request):
    username = request.session.get("username")
    messages = MessageInfo.objects.all()
    if username:
        return render(request, "booklibrary/index.html",{"username":username,"messages":messages})
    else:
        return render(request,"booklibrary/index.html",{"messages":messages})
    # return HttpResponse("shouye")

def user_login(request):
    # form = SLoginForm()
    # context = {
    #     "form": form
    # }
    return render(request,"booklibrary/user_login.html")

def user(request):
    uname = request.session["username"]
    user = Suser.objects.get(username = uname)
    return render(request, "booklibrary/user.html",{"user":user})

def login_tools(request):
    users = Suser.objects.all()
    for user in users:
        if user.username == request.POST["username"]:
            if user.check_password(request.POST['pwd']):
                request.session["username"] = user.username
                print(request.session["username"])
                # return render(request,"booklibrary/user.html",{"user":users})
                return HttpResponseRedirect("/user/", {"user": user})
            else:
                return render(request, "booklibrary/user_login.html", {"error": "密码错误，请重新输入"})
    else:
        return render(request, "booklibrary/user_login.html", {"error": "无该用户，请重新输入"})

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
    # form.set_password(form.password)
    username = request.POST['username']
    form.save()
    user = Suser.objects.get(username = username)
    user.set_password(user.password)
    user.save()
    return render(request, "booklibrary/user_login.html")

def user_info(request):
    uname = request.session["username"]
    user = Suser.objects.get(username = uname)
    return render(request, "booklibrary/user_info.html",{"user":user})

def user_info_update(request,id):
    if request.method == "GET":
        user = Suser.objects.get(pk = id)
        return render(request,"booklibrary/user_info_update.html",{"user":user})
    elif request.method == "POST":
        user = Suser.objects.get(pk = id)
        if len(request.POST["uname"]) == 0:
            user.username=user.username
        else:
            user.username = request.POST["uname"]
        if len(request.POST["pwd"]) == 0:
            user.password=user.password
        else:
            user.password = request.POST["pwd"]
        if len(request.POST["college"]) == 0:
            user.college=user.college
        else:
            user.college = request.POST["college"]
        if len(request.POST["uno"]) == 0:
            user.uno = user.uno
        else:
            user.uno = request.POST["uno"]
        if len(request.POST["email"]) == 0:
            user.email = user.email
        else:
            user.email = request.POST["email"]
        user.save()
        return render(request, "booklibrary/user_info.html", {"user": user})

def querybook(request):
    if request.method == "GET":
        return render(request,"booklibrary/querybook.html")
    elif request.method == "POST":
        item = request.POST["item"]
        query = request.POST["query"]
        if item == "bname":
            books = Book.objects.all().filter(bname__contains = query)
        else:
            books = Book.objects.all().filter(auther__contains = query)
        return render(request,"booklibrary/querybook.html",{"books":books})

def book_info(request,id):
    if request.method == "GET":
        book = Book.objects.get(pk = id)
        borrow = Borrows.objects.all().filter(bname=book).filter(status=True)[0]
        if borrow:
            res = True
        else:
            res = False
        return render(request, "booklibrary/book_info.html", {"book": book,"res":res,"borrow":borrow})
    elif request.method == "POST":
        book = Book.objects.get(pk=id)
        borrows = Borrows()
        uname = request.session["username"]
        user = Suser.objects.get(username=uname)
        borrows.uname = user
        borrows.bname = book
        borrows.status = True
        borrows.date_borrow = datetime.now()
        borrows.date_retur = datetime.now() + timedelta(days=30)
        borrows.save()
        borrow = Borrows.objects.all().filter(bname=book).filter(status=True)

        return HttpResponseRedirect("/book_info/" + str(book.id) + "/", {"book": book,"res":True,"borrow":borrow})

def borrow_info(request):
    uname = request.session["username"]
    user = Suser.objects.get(username=uname)
    borrows = user.borrows_set.all()
    return render(request, "booklibrary/borrow_info.html", {"borrows": borrows})

def edit(request):
    if request.method == "GET":
        return render(request,"booklibrary/edit.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        mes = MessageInfo(title=title,content=content)
        mes.save()
        return HttpResponseRedirect(reverse("library:index"))