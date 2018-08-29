from django.conf.urls import url, include
from django.shortcuts import render

import xadmin as admin

from art.models import Category, Art


def index(request):
    # 查询所有的一级分类
    cates = Category.objects.filter(parent=None).all()

    # 查询所有文章Art
    arts = Art.objects.all()

    return render(request, 'index.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'', index),
]
