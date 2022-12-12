from django.shortcuts import render
from .forms import RegisterForm,setPasswordForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
import logging
from .models import  User
from articles.models import FavoriteVerse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Get an instance of a logger
logger = logging.getLogger(__name__)
from django.utils import translation
from django.http import JsonResponse,HttpResponse
from django.conf import settings
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

    return render(request, 'user/login.html')

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
    return render (request=request, template_name="user/register.html", context={"register_form":form})


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
    
    logger.info('mypage status:',user)
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

    # if request.method == 'GET':
    #         language_code=request.GET.get('language')
    #         # original_language=request.GET.get('django_language')
    #         if language_code:
    #             translation.activate(language_code)
    #             logger.info("language:",language_code)
    #             # user.language=language_code
    #             # user.save()
    favoriteVerses = FavoriteVerse.objects.filter(user=user)
    
    logger.info("verses:",favoriteVerses)
    context={"form":form,
             'status':status,
             'username':username,
             'Verses':favoriteVerses}        
    return render(request,'user/mypage.html',context)
