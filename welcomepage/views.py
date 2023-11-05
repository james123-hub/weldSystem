from django.shortcuts import render, redirect
from .forms import UserRegForm,UserDetailForm
from .models import userInfo,userDetail
from django.urls import reverse

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = userInfo.objects.filter(username=username)
        if user:
            if user[0].password == password:
                url = reverse('userdetail')
                response  = redirect(url)
                response.set_cookie("username",username, 604800)
                return response
            else:
                info = '密码错误！！！'
                return render(request, 'login.html', {"pwdinfo": info})
        else:
            info = '用户名不存在'
            return render(request, 'login.html', {"userinfo": info})
    return render(request, 'login.html')

    return render(request, 'login.html')
def register(request):
    if request.method == "POST":
        form_obj = UserRegForm(request.POST)
        if form_obj.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            if userInfo.objects.filter(username = username):
                info = '用户名已存在'
                return render(request, 'register.html', {"info": info})
            user = userInfo()
            user.username = username
            user.password = password
            user.status = '0'
            user.save()
            url = reverse('login')
            return redirect(url)
        else:
            errors = form_obj.errors
            return render(request, 'register.html', {"errors": errors})
    return render(request, 'register.html')
def home(request):
    return render(request, 'home.html')
def logout(request):
    response = redirect(reverse('homepage'))
    response.delete_cookie("username")
    return response
def getCookie(request):
    return render(request, 'cookie.html')
def getBase(request):
    return render(request, 'usernav.html')
def userDeatail(request):
    if request.method == 'POST':
        form_obj = UserDetailForm(request.POST)
        if form_obj.is_valid():
             username = request.COOKIES['username']
             user = userInfo.objects.get(username = username)
             userdetail = userDetail.objects.get(username = username)
             newuserName = request.POST.get("username")
             if len(newuserName) != 0 and :
                 userDetail.username = newuserName
                 user.username = newuserName
                 user.save()
             userDetail.sex = request.POST.get("sex")

        else:
            errors = form_obj.errors
            return render(request, 'userdetail.html', {"errors": errors})
    return render(request, 'userdetail.html')