from django.shortcuts import render, redirect

from Order.forms import order_form
from .models import Book, Category
from django.http import Http404
from django.views.generic.list import ListView


# Create your views here.

class book_all(ListView):
    queryset = Book.objects.all()
    template_name = 'products.html'
    paginate_by = 6


class book_listview(ListView):
    template_name = 'products.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        category_title = self.kwargs['title']
        context['category'] = category_title
        return context

    def get_queryset(self, *args, **kwargs):
        category_title = self.kwargs['title']
        category_title = category_title.replace('-', ' ')
        qs = Book.objects.filter(category__title=category_title)
        if qs is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Book.objects.filter(category__title=category_title)


def book_detailview(request, *args, **kwargs):
    book_id = kwargs['bookid']
    book = Book.objects.filter(id=book_id).first()
    new_order_form = order_form(request.POST or None,
                                initial={'product_id': book_id, 'product_title': 'book'})
    if book is not None and book.is_exist:
        related_book = Book.objects.filter(category_id=book.category_id)
        visit = Book.objects.get(id=book_id)
        visit.vote += 1
        visit.save()
        context = {
            'book': book,
            'related_book': related_book,
            'new_order_form': new_order_form
        }
        return render(request, 'product_detail.html', context)
    else:
        raise Http404('کالای مورد نظر یافت نشد')


def bookSearch(request, **kwargs):
    products = []
    findProduct = []
    context = {}
    if 'searchBook=all' in request.path:
        book = Book.objects.all()
    else:
        category_title = kwargs['title'].replace('-', ' ')
        category = Category.objects.get(title=category_title)
        book = Book.objects.filter(category_id=category.id)

    for b in book:
        products.append(b)
    qs = request.GET.get('bo')
    if qs is not None and qs.strip() != '':
        for p in products:
            if qs in p.title or qs in p.description:
                findProduct.append(p)
                context['search'] = findProduct
        return render(request, 'search.html', context)
