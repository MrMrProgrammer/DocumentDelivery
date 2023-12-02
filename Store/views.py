from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .models import Store
from .forms import StoreRegisterForm


@login_required
def show_store(request):
    stores = Store.objects.filter(is_delete=False)

    context = {
        'stores': stores,
    }

    return render(request, 'Store/show-stores.html', context)


@method_decorator(login_required, name='dispatch')
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


def delete_store(request, store_id):
    store = Store.objects.filter(id=store_id).first()
    store.is_delete = True
    store.save()

    return redirect('show-store')
