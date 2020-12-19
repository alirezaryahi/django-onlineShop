from itertools import chain

from django.shortcuts import render, redirect
from operator import attrgetter
from Calture.models import Effect, Subject
from Library.models import Book, Category
from Slider.models import Slider
from Stationery.models import Stationery, Group


def home_page(request):
    products = []
    book = Book.objects.all()
    for b in book:
        products.append(b)

    stationery = Stationery.objects.all()
    for s in stationery:
        products.append(s)

    effect = Effect.objects.all()
    for e in effect:
        products.append(e)

    slider = Slider.objects.all()

    products = sorted(
        chain(book, stationery, effect),
        key=attrgetter('vote'),
        reverse=True
    )

    context = {
        'book_list': book,
        'stationery_list': stationery,
        'effect_list': effect,
        'slider': slider,
        'vote': products
    }
    return render(request, 'home.html', context)


def productSearch(request):
    products = []
    findProduct = []
    context = {}
    book = Book.objects.all()
    for b in book:
        products.append(b)

    stationery = Stationery.objects.all()
    for s in stationery:
        products.append(s)

    effect = Effect.objects.all()
    for e in effect:
        products.append(e)

    qs = request.GET.get('q')
    if qs is not None and qs.strip() != '':
        for p in products:
            if qs in p.title or qs in p.description:
                findProduct.append(p)
                context['search'] = findProduct
        return render(request, 'search.html', context)
    else:
        return redirect('/')


def header(request):
    category = Category.objects.all()
    group = Group.objects.all()
    subject = Subject.objects.all()
    context = {}
    if category.count() > 3:
        category = Category.objects.all()[:4]
        category1 = Category.objects.all()[4:8]
        context['category'] = category
        context['category1'] = category1
    else:
        category = Category.objects.all()
        context['category'] = category

    if group.count() > 3:
        group = Group.objects.all()[:3]
        group1 = Group.objects.all()[3:6]
        context['group'] = group
        context['group1'] = group1
    else:
        group = Group.objects.all()
        context['group'] = group

    if subject.count() > 3:
        subject = Subject.objects.all()[:3]
        subject1 = Subject.objects.all()[3:6]
        context['subject'] = subject
        context['subject1'] = subject1
    else:
        subject = Subject.objects.all()
        context['subject'] = subject

    return render(request, 'shared/Header.html', context)
