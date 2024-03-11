from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all()
    return render(request, 'crud_app/index.html', {'items': items})
