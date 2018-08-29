from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render

import xadmin as admin

from art.models import Category, Art


def index(request):
    # 查询所有的一级分类
    cates = Category.objects.filter(parent=None).all()

    # 查询所有文章Art
    arts = Art.objects.all()

    # 实现Art文章的分页
    # 获取请求参数的page页码
    page = request.GET.get('page', '1')

    paginator = Paginator(arts, 10)  # 分页器
    pager = paginator.page(int(page))  # 读取第一页的数据

    return render(request, 'index.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'', index),
]
