

# Create your views here.
from django.shortcuts import render,HttpResponse
from bible.models import Verse,Keyword
import requests
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
import uuid
import os
from random import randint
from datetime import datetime
# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
import logging

# def home(request):
def graphView(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    username=request.COOKIES.get('username')
    # messages.add_message(request, messages.INFO, 'welcome %s'%username)
    # logging.info('cookie: %s'%cookie)
    verses= Verse.nodes.filter(bookID=57)
    # keywords=Keyword.nodes.first(
    return render(request, 'bible/graph.html', {'verses': verses,'status':status})
