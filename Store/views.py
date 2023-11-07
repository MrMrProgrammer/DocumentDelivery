from django.shortcuts import render
from .models import Store


def show_store(request):
    stores = Store.objects.all()

    context = {
        'stores': stores,
    }

    return render(request, 'Store/show-stores.html', context)
