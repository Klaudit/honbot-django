from django.shortcuts import render_to_response
from .models import Items


def main(request):
    items = Items.objects.all().values()
    return render_to_response('items.html', {'items': items})


def item(request, item_id):
    item = Items.objects.filter(item_id=item_id)[0]
    return render_to_response('item.html', {'item': item})