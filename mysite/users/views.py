from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
import logging
from .models import User
from django.contrib import messages

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
            rep = redirect(reverse('article-list'))
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
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful." )
            return redirect(reverse('login'))
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render (request=request, template_name="login/register.html", context={"register_form":form})


# def register(request):
#     pass
#     return render(request,'login/register.html')

def logout(request):
    rep = redirect('login/login')
    rep.delete_cookie("is_login")
    rep.delete_cookie("username")

    messages.add_message(request, messages.INFO, 'please login ')

    return rep
