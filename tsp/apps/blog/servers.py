import time
from django.db.models import Q
from apps.blog.models import *
from apps.utils.commons import *

def getCatalogueById(id=None):
    entity = None
    if (id != None and id != ''):
        set = Catalogue.objects.filter(pk=id)
        if len(set) > 0:
            entity = reverse(set[0])
    return entity

def getCatalogueByFilter(entity):
    if entity != None:
        item = Catalogue.objects.filter(category=entity.category_id, isDelete=False)
        if entity.title != None:
            item = item.filter(title__contains=entity.title)
        if entity.updateTime_from != None and entity.updateTime_to != None:
            item = item.filter(Q(updateTime__gte=entity.updateTime_from) & Q(updateTime__lte=entity.updateTime_to))
        return item.order_by('-updateTime')
    return None

def saveCatalogue(entity):
    if entity != None:
        try:
            if entity.id != None:
                item = Catalogue.objects.get(pk=entity.id)
                entity.createTime = item.createTime
                entity.isDelete = item.isDelete
            entity.updateTime = time.localtime()
            entity.save()
        except Exception as e:
            print(e)
            return False
        return True
    return False

def getCategoryAll():
    return Category.objects.all()