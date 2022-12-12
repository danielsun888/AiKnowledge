from django.urls import path
from . import views
from django.urls import include, path

from django.views.generic import TemplateView
from .views import *
# from articles.views import ArticleDetailView

urlpatterns = [
# path('',views.home, name='home'),
    # url(r'^$', mdeditor_form_view, name='mdeditor-form'),
path('mail', sendMail),
# path('', HomePageView.as_view(), name='home'),
path('socket', socket.as_view()),
path('test', test),


path(r'',views.articleView,name='index'),
# path('<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
# path('<int:pk>', views.post_detail, name='post_detail'),
# url('<int:pk>',views.post_detail,name='post_detail'),
path('<int:pk>/', views.post_detail, name='article-detail'),
# path('category/<int:pk>/',views.categoryView, name='category-detail')
path('keyword', views.keywordView, name='article-keyword'),
path('keywordList', views.keywordList, name='keywordList'),

]