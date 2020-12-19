from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import Contact_form
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login')
def contact_us(request):
    form = Contact_form(request.POST or None)
    user_id = request.user.id
    person = User.objects.get(id=user_id)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        title = form.cleaned_data.get('title')
        message = form.cleaned_data.get('message')
        person.contact_us_set.create(user=user_id, title=title, email=email, message=message)
        form = Contact_form()
    context = {
        'form': form
    }
    return render(request, 'contact_us.html', context)
