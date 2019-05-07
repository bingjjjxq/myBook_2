# -*- coding:utf-8 -*-
__author__ = 'Journey'
__time__ = '2019/5/7 14:50'

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'addbook', Addbook.as_view(), name='addbook'),
]
