# -*- coding: utf-8 -*-
__author__ = 'HeYang'
__time__ = '2018/7/20 21:15'

from django import forms
# 定义组件和样式
from django.forms import widgets

from .models import TypeBook, Publisher, Author


class BookForm(forms.Form):

    name = forms.CharField(
        max_length=32,
        min_length=2,
        widget=widgets.TextInput(
            attrs={"class": 'form-control', "id": 'bookname', "placeholder": "书名"}
        )
    )

    publish_year = forms.DateField(
        widget=widgets.DateInput(
            attrs={"placeholder": "出版日期: 2017-1-1", "class": "form-control", "id": "publish_year"}
        )
    )

    price = forms.IntegerField(
        widget=widgets.NumberInput(
            attrs={"placeholder": "价格", "class": 'form-control', "id": "price"}
        )
    )

    stocks = forms.IntegerField(
        widget=widgets.NumberInput(
            attrs={"placeholder": "库存", "class": 'form-control', "id": "stocks"}
        )
    )

    author = forms.MultipleChoiceField(
        choices=Author.objects.all().values_list('id', 'name'),
        widget=widgets.SelectMultiple(
            attrs={"id": "demo-cs-multiselect"}
        )
    )

    status = forms.ChoiceField(
        choices=[(1, "出版"), (0, '未出版')],
        widget=widgets.Select(
            attrs={"class": "magic-select", "type": "select", "id": 'status', }
        )

    )

    type = forms.ChoiceField(
        choices=TypeBook.objects.all().values_list('id', 'type_book'),
        widget=widgets.Select(
            attrs={"class": "selectpicker", "data-live-search": "true", "data-width": "100%", "id": "type", }
        )
    )

    publisher = forms.ChoiceField(
        choices=Publisher.objects.all().values_list('id', 'name'),
        widget=widgets.Select(
            attrs={"class": "selectpicker", "data-live-search": "true", "data-width": "100%", "id": "publisher", }
        )
    )