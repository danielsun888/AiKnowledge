

from django.conf.urls.static import static
from django.contrib import admin
#from session import views as session_views
from django.conf.urls.i18n import i18n_patterns

# from chat import views as chatview

from django.urls import include, path,re_path

from users import views as user_views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('', include('articles.urls')),
    # re_path('index',  include('articles.urls'),name='index'),
    # path('search/', include('haystack.urls')),
    path('graph/', include('graph.urls')),
    
    path(r'admin/', admin.site.urls),
    
    path('articles/',include('articles.urls')),

    path('tinymce/',include('tinymce.urls')), # new

    path('user/',include('users.urls')),
    # path("search/",MySearchView.as_view()),
    path('search/', include('haystack.urls')),
    # path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),  # NEW

    ##wagtail
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),

    ]
urlpatterns += i18n_patterns(
    # path('admin/', admin.site.urls),
    path('user/',include('users.urls')),

    path('', include('articles.urls')),
)
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)