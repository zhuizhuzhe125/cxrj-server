from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json


# Create your views here.

#------ index -- 首页 ----
def index_slideshow(request):
    ''' 首页轮播图 '''
    user = ['only', '1234']
    res = {
        'mag':'ok',
        'data': user,
    }
    rew = json.dumps(res, indent = 4)
    return HttpResponse(rew, content_type = 'application/json')
