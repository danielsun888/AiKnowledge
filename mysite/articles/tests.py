from django.test import TestCase
from django.utils.translation import get_language
from django.shortcuts import render,redirect

# Create your tests here.
from django.utils.translation import gettext as _
from django.http import HttpResponse,JsonResponse
import logging
logger = logging.getLogger(__name__)

def my_view(request):

 

    # for i,word in enumerate(words) :
    #     name='output[%d]' % i
    #     output[name]=gettext(word)
    return render(request, 'articles/test.html')
    return JsonResponse({1:_('Testament'),2:_("Books"),3:_("Chapters"),4:_("Submit"),5:_("Please select book first"),\
        6:_("Please select chapter first"),7:_("first"),8:_("previous"),9:_("next"),10:_("last")})

import json

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ajax_test_add(request):
    a = int(request.POST.get('a'))
    b = int(request.POST.get('b'))
    return_json = {'result':a+b}
    return HttpResponse(json.dumps(return_json), content_type='application/json')

from articles.models import *
def index(request):
    posts = Articles.objects.all()[:10]  # Getting all the posts from database
    # return HttpResponse(json.dumps(posts), content_type='application/json')
    return render(request, 'articles/test.html', { 'posts': posts })

def likepost(request):
    if request.method == 'GET':
           post_id = request.GET['post_id']
           likedpost = Articles.objects.get(pk=post_id) #getting the liked posts
           logger.info('like:',post_id)
           m = FavoriteVerse(verse=likedpost) # Creating Like Object
           m.save()  # saving it to store in database
           return HttpResponse("Success!") # Sending an success response
    else:
           return HttpResponse("Request method is not a GET")