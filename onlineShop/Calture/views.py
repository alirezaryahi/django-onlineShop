from django.shortcuts import render
from django.views.generic import ListView
from .models import Effect, Subject
from django.http import Http404
from Order.forms import order_form


# Create your views here.

class Caltute_all(ListView):
    queryset = Effect.objects.all()
    template_name = 'efects.html'
    paginate_by = 6


class Calture_listview(ListView):
    template_name = 'efects.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        category_title = self.kwargs['title']
        context['category'] = category_title
        return context

    def get_queryset(self, *args, **kwargs):
        category_title = self.kwargs['title']
        category_title = category_title.replace('-', ' ')
        qs = Effect.objects.filter(subject__title=category_title)
        if qs is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Effect.objects.filter(subject__title=category_title)


def Calture_detailview(request, *args, **kwargs):
    efect_id = kwargs['efectid']
    effect = Effect.objects.filter(id=efect_id).first()
    new_order_form = order_form(request.POST or None, initial={'product_id': efect_id, 'product_title': 'effect'})
    if effect is not None and effect.is_exist:
        related_efect = Effect.objects.filter(subject_id=effect.subject_id)
        visit = Effect.objects.get(id=efect_id)
        visit.vote += 1
        visit.save()
        context = {
            'effect': effect,
            'related_effect': related_efect,
            'new_order_form': new_order_form
        }
        return render(request, 'efect_detail.html', context)
    else:
        raise Http404('کالای مورد نظر یافت نشد')

def CaltureSearch(request, **kwargs):
    products = []
    findProduct = []
    context = {}
    if 'searchCalture=all' in request.path:
        effect = Effect.objects.all()
    else:
        subject_title = kwargs['title'].replace('-', ' ')
        subject = Subject.objects.get(title=subject_title)
        effect = Effect.objects.filter(subject_id=subject.id)

    for b in effect:
        products.append(b)
    qs = request.GET.get('ef')
    if qs is not None and qs.strip() != '':
        for p in products:
            if qs in p.title or qs in p.description:
                findProduct.append(p)
                context['search'] = findProduct
    return render(request, 'search.html', context)
