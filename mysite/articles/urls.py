from django.urls import path
from . import views
from django.urls import include, path,re_path as url

from django.views.generic import TemplateView
from .views import *
# from articles.views import ArticleDetailView
from .tests import likepost,index
urlpatterns = [
# path('',views.home, name='home'),
    # url(r'^$', mdeditor_form_view, name='mdeditor-form'),
path('mail', sendMail),
# path('', HomePageView.as_view(), name='home'),
path('socket', socket.as_view()),
# path('test', tests.my_view),

path(r'',views.articleView,name='index'),

path('<int:pk>/', views.post_detail, name='article-detail'),
# path('category/<int:pk>/',views.categoryView, name='category-detail')
path('keyword', views.keywordView, name='article-keyword'),
path('keywordList', views.keywordList, name='keywordList'),
url(r'^likepost', views.likePost, name='likepost'),   # likepost view at /likepost

# path(r'likepost/<int:pk>/', likepost, name='likepost'),   # likepost view at /likepost
path(r'test', views.ajax, name='test'),  # index view at /

]
