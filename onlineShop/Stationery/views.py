from django.shortcuts import render
from django.views.generic import ListView

from Order.forms import order_form
from .models import Stationery, Group
from django.http import Http404


# Create your views here.

class stationery_all(ListView):
    queryset = Stationery.objects.all()
    template_name = 'stationery.html'
    paginate_by = 6


class stationery_listview(ListView):
    template_name = 'stationery.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        category_title = self.kwargs['title']
        context['category'] = category_title
        return context

    def get_queryset(self, *args, **kwargs):
        category_title = self.kwargs['title']
        category_title = category_title.replace('-', ' ')
        qs = Stationery.objects.filter(group__title=category_title)
        if qs is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Stationery.objects.filter(group__title=category_title)


def stationery_detailview(request, *args, **kwargs):
    stationery_id = kwargs['stationeryid']
    stationery = Stationery.objects.filter(id=stationery_id).first()
    new_order_form = order_form(request.POST or None, initial={'product_id': stationery_id, 'product_title': 'stationery'})
    if stationery is not None and stationery.is_exist:
        related_stationery = Stationery.objects.filter(group_id=stationery.group_id)
        visit = Stationery.objects.get(id=stationery_id)
        visit.vote += 1
        visit.save()
        context = {
            'stationery': stationery,
            'related_stationery': related_stationery,
            'new_order_form': new_order_form
        }
        return render(request, 'stationery_detail.html', context)
    else:
        raise Http404('کالای مورد نظر یافت نشد')


def StationerySearch(request, **kwargs):
    products = []
    findProduct = []
    context = {}
    if 'searchStationery=all' in request.path:
        stationery = Stationery.objects.all()
    else:
        group_title = kwargs['title'].replace('-', ' ')
        group = Group.objects.get(title=group_title)
        stationery = Stationery.objects.filter(group_id=group.id)

    for b in stationery:
        products.append(b)
    qs = request.GET.get('st')
    if qs is not None and qs.strip() != '':
        for p in products:
            if qs in p.title or qs in p.description:
                findProduct.append(p)
                context['search'] = findProduct
                print(findProduct)
        return render(request, 'search.html', context)
