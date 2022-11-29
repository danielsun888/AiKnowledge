from django.shortcuts import render
import logging

# Create your views here.
from django.shortcuts import render,HttpResponse
from .models import *
import requests
from django.shortcuts import render,redirect
from django.forms import Form, fields, widgets
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
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from .forms import  CommentForm
from django.core.paginator import Paginator

from django.contrib import messages

logger = logging.getLogger(__name__)

# def home(request):
#     # categories = Category.objects.all()
#     articles = Articles.objects.all()
#     # for x in images:
#     #     x.shortDescription = x.description[:130]
#     context = {}
#     # context['categories'] = categories
#     context['articles'] = articles

#     return render(request, 'articles/index.html', context)
#     # return HttpResponse("Hello, world. You're at the polls index.")
class socket(TemplateView):

    template_name = "articles/socket.html"






def sendMail(request):
    # create a variable to keep track of the form
    messageSent = False
    # check if form has been submitted
    if request.method == 'POST':
        form = EmailForm(request.POST)
        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = cd['message']
            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])
            # set the variable initially created to True
            messageSent = True
    else:
        form = EmailForm()
    return render(request, 'articles/mail.html', {
        'form': form,
        'messageSent': messageSent,
    })


# class ArticleListView(ListView):
#     template_name = 'articles/article-list.html'
#     articles = Articles.objects.get_queryset().order_by('last_updated')
#     Categories=Category.objects.all()
#     model = Articles
#     paginate_by = settings.PAGINATE_BY
#     # paginate_by = 10

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         context['articles'] = self.articles
#         context['categories'] = self.Categories

#         return context
def articleView(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    # if not status:
    #     return redirect('/login/login/')
    username=request.COOKIES.get('username')
    articles= Articles.objects.all().order_by('id')
    paginate_by = settings.PAGINATE_BY

    paginator = Paginator(articles, paginate_by) # 每页显示25条

    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    return render(request, 'articles/article-list.html', {'articles': article_list,'status':status,'username':username})

# class CategoryListView(ListView):
#     template_name = 'articles/category-detail.html'
    
#     model = Category
#     paginate_by = settings.PAGINATE_BY

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Articles.objects.filter(**kwargs)
#         # queryset = Articles.objects.all()
#         # context['articles'] = Articles.objects.all()

#         context['now'] = timezone.now()
#         # context['articles'] = self.articles

#         return context

def categoryView(request, pk):
    # 记得在开始部分导入 Category 类
    category = get_object_or_404(Category, pk=pk)
    post_list = Articles.objects.filter(category=category).order_by('-date_created')
    # context={}
    # context['articles'] = post_list

    categories = Category.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')   
    page_obj = paginator.get_page(page_number)
    # page_obj['categories'] = Category.objects.all()
    return render(request, 'articles/category-detail.html', context={'page_obj': page_obj,'categories':categories} )

    # def get_queryset(self):
    #     return self.object.Articles.all()
# class ArticleDetailView(DetailView):
#     template_name = 'articles/article-detail.html'

#     model = Articles

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # comments_connected = Comment.objects.filter(article=self.get_object()).order_by('-date_posted')
#         # context['comments'] = comments_connected
#         context['now'] = timezone.now()
#         context['categories'] = Category.objects.all()

#         return context




def post_detail(request, pk):
            categories = Category.objects.all()

            post   = get_object_or_404(Articles, id=pk)
            comments  = post.comments.filter(active=True)

            # print comments	
            # for comment in comments:
            # 	for reply in comment.replies.all():
            # 		print reply.body
            # 		# print reply.__dict__
            # rpy = Comment.objects.filter(active=True)	
            if request.method == 'POST':
                comment_form = CommentForm(data=request.POST)
                if comment_form.is_valid():
                    new_comment = comment_form.save(commit=False)
                    # Assign the current post to the comment
                    new_comment.post = post
                    # Save the comment to the database
                    new_comment.save()
            else:
                comment_form = CommentForm()

            context = {
                'categories': categories,
                'post':post,
                'comments': comments,
                'comment_form': comment_form
            }

            return render(request,'articles/article-detail.html',context)