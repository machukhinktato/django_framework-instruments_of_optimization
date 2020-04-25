"""from django.urls import path
from django.urls import re_path
from django.views.decorators.cache import cache_page
import os
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>/ajax/', cache_page(3600)(
        mainapp.products_ajax), name='category_ajax'),
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('category/<int:pk>/page/<int:page>', mainapp.products, name='page'),
    path('category/<int:pk>/page/<int:page>/ajax/', cache_page(3600)(
        mainapp.products_ajax)),
]"""
# from django.conf.urls import url

import mainapp.views as mainapp
from django.urls import re_path

from django.views.decorators.cache import cache_page

app_name = "mainapp"

urlpatterns = [
    re_path(r'^$', mainapp.products, name='index'),
    re_path(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'),
    re_path(r'^category/(?P<pk>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),

    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),

]

