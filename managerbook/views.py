from django.shortcuts import render
from django.views.generic import ListView

from managerbook.models import *

# Create your views here.

class index(ListView):
    """
    首页 书籍列表 查询功能
    """
    template_name = 'book.html'
    model = Book
    context_object_name = 'book_obj'