from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from apps.blog.servers import *
from apps.blog.models import *
from apps.base.models import *

# Create your views here.

def catalogueInit(request, action='', category_id='', id=''):
    context = {
        'id': id,
        'action': action,
        'catalogue': getCatalogueById(id),
        'category_id': category_id,
    }
    return render(request, 'blog_info.html', context)

@mirror(Catalogue())
def catalogueSave(request, entity=None):
    flag = saveCatalogue(entity)
    return HttpResponse("SUCCESS") if flag else HttpResponse("ERROR")

def catalogueList(request, category_id=None, page_number=None):
    context = {
        'category_id': category_id if category_id!=None and category_id!='' else '1',
        'page_number': page_number if page_number!=None and page_number!='' else '1',
        'page_limit': '2',
    }
    return render(request, 'blog_list.html', context)

@mirror(Catalogue())
def catalogueListData(request, entity=None, page_limit='25', page_number='1'):
    item = getCatalogueByFilter(entity)
    page = SimplePage().writeSimplePage(item, page_limit, page_number)
    page.page_object_list = json.dumps(opposite(page.page_object_list))
    return HttpResponse(json.dumps(reverse(page)), content_type='application/json')

def categoryAllList(request):
    context = getCategoryAll()
    return HttpResponse(json.dumps(opposite(context)), content_type='application/json')