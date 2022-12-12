from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView
# from users2 import views
# from articles.views import ArticleDetailView



urlpatterns = [
    # path(r'^index/', views.index),
    path("mypage/",views.mypage, name="mypage"),
    re_path(r'login/', views.login,name='login'),
    re_path(r'register/', views.register,name='register'),
    path(r'logout/', views.logout,name='logout'),
]