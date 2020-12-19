from django.shortcuts import render, redirect
from .forms import Login_form, Register_form, User_edit, User_edit_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Custom_User


# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = Login_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form.add_error('username', 'کاربری با این مشخصات یافت نشد')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = Register_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                 password=password, is_superuser=True, is_active=True, is_staff=True)
        user = User.objects.get(username=username)
        Custom_User.objects.create(user_id=user.id, phone=phone)
        return redirect('/login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def log_out(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def user_info(request):
    User = get_user_model()
    user_id = request.user.id
    user_detail = User.objects.get(id=user_id)
    user_phone = Custom_User.objects.get(user__id=user_id)
    context = {
        'user_detail': user_detail,
        'user_phone': user_phone
    }
    return render(request, 'user_info.html', context)


@login_required(login_url='/login')
def user_edit(request):
    user_id = request.user.id
    user_detail = User.objects.get(id=user_id)

    context = {}
    user_phone = Custom_User.objects.get(user__id=user_id)

    form = User_edit(request.POST or None,
                     initial={'first_name': user_detail.first_name, 'last_name': user_detail.last_name,
                              'phone': user_phone.phone, 'email': user_detail.email})
    context['form'] = form

    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        user_detail.first_name = first_name
        user_detail.last_name = last_name
        user_detail.email = email
        user_phone.phone = phone
        user_detail.save()
        user_phone.save()

    return render(request, 'user_edit.html', context)


@login_required(login_url='/login')
def user_edit_password(request):
    User = get_user_model()
    user_id = request.user.id
    user_detail = User.objects.get(id=user_id)
    user = User.objects.get(username__exact=user_detail.username)
    form = User_edit_password(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
    context = {
        'form': form
    }
    return render(request, 'user_edit_password.html', context)
