from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse

from managerbook.models import *
from managerbook.form import BookForm

# from pure_pagination import Paginator

# Create your views here.


# class index(View):
#
#     def get(self, request):
#         book_obj = Book.objects.all()
#
#         return render(request, 'book.html', {
#             'book_obj': book_obj
#         })


class Addbook(ListView):
    template_name = 'add_book.html'
    model = Book
    context_object_name = 'book_obj'

    def get_queryset(self):
        quryset = super(Addbook, self).get_queryset()

        page = self.request.GET.get('page', 1)
        p = Paginator(quryset, 10)
        people = p.page(page)

        return people


    def get_context_data(self, **kwargs):
        book_form = BookForm()
        context = super(Addbook, self).get_context_data()

        context['book_form'] = book_form

        return context

    def post(self, request):
        ret = {"status": "", "data": ""}
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_data = book_form.cleaned_data
            book = Book()
            book.name = book_data['name']
            book.publish_year = book_data['publish_year']
            book.price = book_data['price']
            book.stocks = book_data['stocks']
            book.status = book_data['status']
            book.type_id = book_data['type']
            book.publisher_id = book_data['publisher']
            book.save()

            book.author.add(*book_data['author'])

            ret['status'] = "success"
            ret['data'] = '书籍添加成功'

            return JsonResponse(ret)
        else:
            ret['data'] = book_form.errors

            return JsonResponse(ret)

class index(ListView):
    """
    首页 书籍列表 查询功能
    """
    template_name = 'book.html'
    # Book.objects.all()
    model = Book
    context_object_name = 'book_obj'

    def get_queryset(self):
        # super代表，调用父类的
        queryset = super(index, self).get_queryset()
        # queryset == Book.objects.all()
        # queryset 就是等同于，取出Book表中所有的值

        # page = self.request.GET.get('page', 1)
        #
        # # 第一个参数 数据[] list,
        # # 第二个参数 request  请求
        # # 第三个参数 一页展示多少条
        # p = Paginator(queryset, request=self.request, per_page=10)
        #
        # people = p.page(page)
        page = self.request.GET.get('page', 1)

        self.is_type = self.request.GET.get('type', '')
        self.is_status = self.request.GET.get('status', '')
        self.search = self.request.GET.get('search', '')

        # Q 多种条件查询
        #  and == &
        #  or == |

        if self.is_type and self.is_status:
            queryset = self.model.objects.filter(
                (Q(name__icontains=self.search) | Q(author__name__icontains=self.search))
                & Q(type=self.is_type) & Q(status=self.is_status)
            ).distinct()
        elif self.is_type:
            queryset = self.model.objects.filter(
                (Q(name__icontains=self.search) | Q(author__name__icontains=self.search))
                & Q(type=self.is_type)
            ).distinct()
        elif self.is_status:
            queryset = self.model.objects.filter(
                (Q(name__icontains=self.search) | Q(author__name__icontains=self.search))
                & Q(status=self.is_status)
            ).distinct()
        elif self.search and (self.is_type == '' and self.is_status == ''):
            queryset = self.model.objects.filter(
                (Q(name__icontains=self.search) | Q(author__name__icontains=self.search))
            ).distinct()


            # people = Book.objects.filter(
            #     Q(name__icontains=search) | Q(author__name__icontains=search)
            # )

        print(self.request.GET)
        p = Paginator(queryset, 2)

        people = p.page(page)

        return people

    def get_context_data(self, **kwargs):
        """
        在默认的上下返回前端的基础上，增加上下文信息
        可以返回给前端更多的变量
        :param kwargs:
        :return:
        """

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
            pass

        context['search'] = self.search

        print(context)
        return context