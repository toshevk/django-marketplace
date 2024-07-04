from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Item
from .forms import NewItemForm


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request=request, template_name='item/detail.html', context={
        'item': item,
        'related_items': related_items
    })


@login_required
def new_item(request):
    form = NewItemForm()

    return render(request=request, template_name='item/form.html', context={
        'form': form,
        'title': 'New item'
    })
