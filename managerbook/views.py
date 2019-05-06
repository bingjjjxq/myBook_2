from django.shortcuts import render
from django.views.generic import ListView,View
from django.core.paginator import Paginator
from django.db.models import Q

from managerbook.models import *

# class index(View):
#
#     def get(self, request):
#         book_obj = Book.objects.all()
#
#         return render(request, 'book.html', {'book_obj':book_obj})

class index(ListView):
    """
    首页 书籍列表 查询功能
    """
    template_name = 'book.html'
    model = Book
    context_object_name = 'book_obj'

    def get_queryset(self):
        # super代表，调用父类的
        queryset = super(index, self).get_queryset() #去除Book表中所有的值
        print(queryset)

        page = self.request.GET.get('page', 1)

        self.is_type = self.request.GET.get('type', '')
        self.is_status = self.request.GET.get('status', '')
        self.search = self.request.GET.get('search', '')

        # Q 多重条件查询 and or

        if self.is_type and self.is_status:
            queryset = self.model.objects.filter(        #等同于people = Book.objects.filter
                (Q(name__icontains=self.search) | Q(author__name__icontains=self.search))
                & Q(type=self.is_type) & Q(status=self.is_status)
            )
        elif self.is_type:
            queryset = self.model.objects.filter(
                (Q(name__icontains=self.search) | Q(author__name__icontains=self.search))
                & Q(type=self.is_type)
            )
        elif self.is_status:
            queryset = self.model.objects.filter(
                (Q(name__icontains=self.search) | Q(author__name__icontains=self.search))
                & Q(status=self.is_status)
            )
        elif self.search:
            queryset = self.model.objects.filter(
                Q(name__icontains=self.search) | Q(author__name__icontains=self.search)
            )

        print(self.request.GET)
        p = Paginator(queryset, 2)     #生成分页

        people = p.page(page)

        return people

    def get_context_data(self, **kwargs):
        # 在默认的上下文返回前端的基础上，增加上下文信息
        # 可以返回给前端更多的变量
        type_all = TypeBook.objects.all()
        context = super(index, self).get_context_data(**kwargs)
        context['type_all'] = type_all
        try:
            context['is_type'] = int(self.is_type)
        except:
            context['is_type'] = ''
        try:
            context['is_status'] = int(self.is_status)
        except:
            context['is_status'] = ''

        context['search'] = self.search

        print(context)
        return context
