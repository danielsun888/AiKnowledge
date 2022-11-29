



from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
#from session import views as session_views
from django.urls import include
from django.contrib.auth.views import LoginView,LogoutView
from users import views as user_views

# from chat import views as chatview


from django.views.decorators.csrf import csrf_exempt

from django.urls import include, path,re_path

#flipbook
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


urlpatterns = [

    path('', include('articles.urls')),
    re_path('index',  include('articles.urls'),name='index'),
    path('search/', include('haystack.urls')),
    path('graph/', include('bible.urls')),
    path(r'admin/', admin.site.urls),
    
    path('articles/',include('articles.urls')),

    path('tinymce/',include('tinymce.urls')), # new

    path('login/',include('users.urls')),
    ]
