# -*- coding:utf-8 -*-
__author__ = 'Journey'
__time__ = '2019/5/7 14:50'

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'addbook', Addbook.as_view(), name='addbook'),
    url(r'create_details', Create_Details.as_view(), name='create_details'),
    url(r'book_del', Book_Del.as_view(), name='book_del'),
]
