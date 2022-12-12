from django.shortcuts import render
import logging
from django.core import serializers
import datetime

# Create your views here.
from django.shortcuts import render,HttpResponse
from .models import *
from django.shortcuts import render,redirect
from django.forms import Form, fields, widgets
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail

from django.shortcuts import render, get_object_or_404
from .forms import  CommentForm,BookForm
from django.core.paginator import Paginator

from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse,HttpResponse

logger = logging.getLogger(__name__)
# def index(request):
#     context = {'msg': _("Welcome to China")}
#     return render(request, 'myapp/index.html', context)

def articleView(request):

    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    # if not status:
    #     return redirect('/login/login/')
    username=request.COOKIES.get('username')
    chapters= Chapters.objects.all()

    ## pagination
    paginate_by = 1

    
    # make bible data for form
    newBooks=list(Book.objects.filter(id__gte=40).values())
    newTestament={}
    for i in newBooks:
        newTestament[i['name']]=list(range(1,i['totalChapters']+1))

    oldBooks=list(Book.objects.filter(id__lte=39).values())
    oldTestament={}
    for i in oldBooks:
        oldTestament[i['name']]=list(range(1,i['totalChapters']+1))
    books={'oldTestament':oldTestament,'newTestament':newTestament}

  
    if request.method == 'GET':


        paginator = Paginator(chapters, paginate_by) # 每页显示25条
        chapter_number = request.GET.get('chapter')
        page_obj = paginator.get_page(chapter_number)
        chapter=page_obj.object_list[0]
        logger.info('chapter:',chapter)
        article_list=Articles.objects.filter(chapter=chapter)

        #keyword 
        keywords=[]
        for article in article_list:
            keywords.append(list(article.manyKeywords.all().values()))
        keywordList=[keyword for row in keywords for keyword in row]
      
        # verses=Verse.nodes.filter(BookName=bookName,chapterID=chapterID)
        context={'articles': article_list,
                 'status':status,
                 'username':username,
                 'page_obj': page_obj,
                 'books':books,
                 'keywordList':keywordList,
                 }
     
        return render(request, 'articles/article-list.html', context)
    
    if request.method == 'POST':

        book = request.POST.get('book').strip()
        chapterNumber = request.POST.get('chapter')

        #pagination
        # page_number = request.GET.get('page')

    
        chapter=Chapters.objects.filter(bookName=book,chapterID=chapterNumber)
        # if chapter.exists():
        #    return JsonResponse({'book':book,'chapterNumber':chapterNumber,'chapter':list(chapter.values())})
        # else:
        #      return JsonResponse({'book':book,'chapterNumber':chapterNumber,'books':books})
        chapterID=chapter.values()[0]['id']-1
        logger.info('book:',book,chapterID)

        article_list=Articles.objects.filter(chapter=chapterID)
        # keyword LIST
        keywords=[]
        for article in article_list:
            keywords.append(list(article.manyKeywords.all().values()))
        keywordList=[keyword for row in keywords for keyword in row]
        logger.info('keywordList:',keywordList)
    
        paginator = Paginator(chapters, paginate_by) 
        page_obj = paginator.get_page(chapterID)
        logger.info('book:',book,chapterNumber,chapterID)
        context= {  'articles': article_list,
                    'status':status,
                    'username':username,
                    'page_obj': page_obj,
                    'books':books,
                    'keywordList':keywordList}

        return render(request, 'articles/article-list.html',context)

def keywordView(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    username=request.COOKIES.get('username')

    pk=request.GET.get('id')
    keyword=Keyword.objects.get(id=pk)
    articles=keyword.articles_set.all()

    paginator = Paginator(articles, 50)
    page_number = request.GET.get('page')   
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/keyword_articles.html',context= {'page_obj':page_obj,'articles': articles,'keyword':keyword,'status':status,'username':username})
    # categories = Book.objects.all()
  
    # page_obj['categories'] = Category.objects.all()
    # return render(request, 'articles/category-detail.html', context={'page_obj': page_obj,'categories':categories} )

def keywordList(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    username=request.COOKIES.get('username')

    keywords=Keyword.objects.all().order_by('-frequency')[:500]

    # paginator = Paginator(articles, 50)
    # page_number = request.GET.get('page')   
    # page_obj = paginator.get_page(page_number)
    return render(request, 'articles/keywordList.html',context= {'keywords':keywords,'status':status,'username':username})
  




def post_detail(request, pk):
            status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
            username=request.COOKIES.get('username')
            categories = Book.objects.all()

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
                'comment_form': comment_form,
                'status':status,'username':username
            }

            return render(request,'articles/article-detail.html',context)

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
class socket(TemplateView):

    template_name = "articles/socket.html"

# def add_favorite(request):
#     user = request.user
#     verseID= request.POST['verseID']
#     verse = Articles.objests.get(id=verseID)
#     created_on = datetime.datetime.now()
#     FavoriteVerse.objects.update_or_create(user=user,verse=verse,created_on=created_on)

def likePost(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    
    if request.method == 'GET':
           post_id = request.GET['post_id']
           username=request.COOKIES.get('username')
           user=User.objects.filter(username=username)[0]
           likedpost = Articles.objects.get(id=post_id) #getting the liked posts
           favoriteVerse=FavoriteVerse.objects.filter(verse=likedpost,user=user)
           if favoriteVerse.count()==0:
               logger.info('username and verse:',user,likedpost)

               m = FavoriteVerse(verse=likedpost,user=user) # Creating Like Object

               m.save()  # saving it to store in database
               return HttpResponse("Success!") # Sending an success response
           else:
                return HttpResponse("already liked!") # Sending an success response

    else:
           return HttpResponse("Request method is not a GET")

def ajax(request):
    posts = Articles.objects.all()[:10]  # Getting all the posts from database
    return render(request, 'articles/test.html', { 'posts': posts })