from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *
# from articles.views import ArticleDetailView

urlpatterns = [
    url(r'^register/', views.register, name='register'),]
