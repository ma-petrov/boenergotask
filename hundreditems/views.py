from django.shortcuts import render

from .forms import ItemForm
from .models import Item, Color

def hundred_items(request):
    max_items = Color.get_max_items()

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item_id']
            color = Item.guess_color(item_id)
            item_stat = Item.get_item_stat()
            context = dict(form=form, color=color, item_stat=item_stat, max_items=max_items)
            return render(request, 'hundred_items.html', context)
    else:
        form = ItemForm()
        item_stat = Item.get_item_stat()

    context = dict(form=form, item_stat=item_stat, max_items=max_items)
    return render(request, 'hundred_items.html', context)
