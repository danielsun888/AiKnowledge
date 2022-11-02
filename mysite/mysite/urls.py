"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
#from session import views as session_views
from django.urls import include
from django.contrib.auth.views import LoginView,LogoutView


# from chat import views as chatview


from django.views.decorators.csrf import csrf_exempt

from django.urls import include, path

#flipbook
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


urlpatterns = [

    path('', include('articles.urls')),
    path('index',  include('articles.urls')),
    path('search/', include('haystack.urls')),



    path(r'admin/', admin.site.urls),
    


    path('articles/',include('articles.urls')),

    path('tinymce/',include('tinymce.urls')), # new


    path('accounts/login/',  LoginView.as_view()),
    path('accounts/logout/', LogoutView.as_view()),
       ]

