import logging

from django.shortcuts import render
from django.views.generic import View

from .models import Book

logger = logging.getLogger(__name__)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'book_list': Book.objects.all(),
        }
        return render(request, 'shop/book_list.html', context)


index = IndexView.as_view()
