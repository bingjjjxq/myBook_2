# -*- coding:utf-8 -*-
__author__ = 'Journey'
__time__ = '2019/5/5 14:28'
from django.shortcuts import render

def test(request):

    return render(request,'base.html')