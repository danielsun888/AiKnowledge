

from django.conf.urls.static import static
from django.contrib import admin
#from session import views as session_views
# from django.conf.urls.i18n import i18n_patterns

# from chat import views as chatview

from django.urls import include, path,re_path

from users2 import views as user_views

urlpatterns = [
    path('', include('articles.urls')),
    # re_path('index',  include('articles.urls'),name='index'),
    # path('search/', include('haystack.urls')),
    path('graph/', include('graph.urls')),
    
    path(r'admin/', admin.site.urls),
    
    path('articles/',include('articles.urls')),

    path('tinymce/',include('tinymce.urls')), # new

    path('login/',include('users2.urls')),
    path("mypage/",user_views.mypage, name="mypage"),
    # path("search/",MySearchView.as_view()),
    path('search/', include('haystack.urls')),
    # path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),  # NEW


    ]
# urlpatterns += i18n_patterns(
#     path('admin/', admin.site.urls),
#     path('', include('myapp.urls')),
# )