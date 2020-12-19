from django.shortcuts import render, redirect
from Calture.models import Effect
from Library.models import Book
from Order.models import Order, Order_detail
from Stationery.models import Stationery
from .forms import order_form
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.

@login_required(login_url='/login')
def add_user_order(request):
    form = order_form(request.POST or None)
    if form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if not order:
            print('no')
            Order.objects.create(owner_id=request.user.id, is_paid=False)
        product_id = form.cleaned_data.get('product_id')
        product_title = form.cleaned_data.get('product_title')

        if product_title == 'book':
            product = Book.objects.get(id=product_id)
            order.order_detail_set.create(order_id=order.id, book_id=product.id)
            return redirect(f'books/{product.id}/{product.title.replace(" ", "-")}')

        if product_title == 'stationery':
            product = Stationery.objects.get(id=product_id)
            order.order_detail_set.create(order_id=order.id, stationery_id=product.id)
            return redirect(f'stationeries/{product.id}/{product.title.replace(" ", "-")}')

        if product_title == 'effect':
            product = Effect.objects.get(id=product_id)
            order.order_detail_set.create(order_id=order.id, effect_id=product.id)
            return redirect(f'arts/{product.id}/{product.title.replace(" ", "-")}')
    else:
        return redirect('/')


@login_required(login_url='/login')
def Open_order(request):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    context = {
        'order': None,
        'details': None,
        'total': 0
    }
    if order is not None:
        context['order'] = order
        context['details'] = order.order_detail_set.all()
        context['total'] = order.get_total_price()
    return render(request, 'open_order.html', context)


@login_required(login_url='/login')
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order = Order_detail.objects.get(id=detail_id, order__owner_id=request.user.id)
        if order is not None:
            order.delete()
            return redirect('/openOrder')
    raise Http404('سفارش مورد نظر یافت نشد')
