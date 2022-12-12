from django.shortcuts import render
from .forms import RegisterForm,setPasswordForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
import logging
from .models import User2 as User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

def login(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    logger.info('logging status:',status)

    if request.method == "POST":
       username = request.POST.get('username')
       logger.info('username:',username)

       password = request.POST.get('password')       
       logger.info('password:',password)
 
       user_obj = auth.authenticate(username=username, password=password)
       logger.info('user_obj:',user_obj)
       if not user_obj:
           return redirect('login/login')
       else:

            auth.login(request, user_obj)
            # print(user_obj)
            rep = redirect(reverse('index'))
            rep.set_cookie("is_login", True)
            rep.set_cookie('username', user_obj.username)

            messages.add_message(request, messages.INFO, 'welcome ' )

       return rep
            # return redirect(reverse('article-list'))

    return render(request, 'login/login.html')

def register(request):
    if  request.method == "POST":
        form = RegisterForm(request.POST)
        if  form.is_valid():
            form.save()
            # login(request, user)
            messages.success(request, "Registration successful." )
            return redirect(reverse('login'))
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render (request=request, template_name="login/register.html", context={"register_form":form})


# def register(request):
#     pass
#     return render(request,'login/register.html')
# @login_required
def logout(request):
    rep = redirect('login/login')
    rep.delete_cookie("is_login")
    rep.delete_cookie("username")

    messages.add_message(request, messages.INFO, 'please login ')

    return rep

@login_required
def mypage(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    username=request.COOKIES.get('username')
    user = request.user
    if request.method == 'POST':
        form = setPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect(reverse('login'))
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = setPasswordForm(user)
    return render(request,'login/mypage.html',context={"form":form,'status':status,'username':username})
