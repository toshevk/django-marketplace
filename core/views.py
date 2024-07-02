from django.shortcuts import render
from item.models import Item, Category
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request=request, template_name='core/index.html', context={
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    form = SignupForm()

    return render(request=request, template_name='core/signup.html', context={
        'form': form
    })
