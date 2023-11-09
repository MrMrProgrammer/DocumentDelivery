from django.shortcuts import render, redirect
from django.views import View
from .models import Store
from .forms import StoreRegisterForm


def show_store(request):
    stores = Store.objects.all()

    context = {
        'stores': stores,
    }

    return render(request, 'Store/show-stores.html', context)


class StoreRegisterView(View):

    def get(self, request):
        register_form = StoreRegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'Store/add-store.html', context)

    def post(self, request):

        print('post')

        register_form = StoreRegisterForm(request.POST)

        if register_form.is_valid():

            store_name = register_form.cleaned_data.get('store_name')

            new_store = Store(
                store_name=store_name,
                is_active=True,
            )

            new_store.save()

            return redirect('show-store')

        # context = {
        #     'register_form': register_form,
        # }
        #
        # return render(request, 'Store/add-store.html', context)
