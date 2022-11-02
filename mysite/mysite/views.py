from django.http import HttpResponse
from django.template import response
from django.shortcuts import render,redirect
import json
from django.http import HttpResponse,JsonResponse


from django.http import HttpResponse

from django.template.response import TemplateResponse
import datetime


from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



