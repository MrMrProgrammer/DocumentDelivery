from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .models import Store
from .forms import StoreRegisterForm
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .forms import UpdateStoreForm


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
        register_form = StoreRegisterForm(request.POST)

        if register_form.is_valid():
            store_name = register_form.cleaned_data.get('store_name')
            is_active = register_form.cleaned_data.get('is_active')

            new_store = Store(
                store_name=store_name,
                is_active=is_active,
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


class UpdateStoreView(View):

    def get(self, request: HttpRequest, store_id):
        current_store: Store = Store.objects.filter(id=store_id).first()

        edit_form = UpdateStoreForm(instance=current_store)

        context = {
            'edit_form': edit_form,
            'store_id': store_id,
        }

        return render(request, 'Store/update-store.html', context)

    def post(self, request: HttpRequest, store_id):
        current_store: Store = Store.objects.filter(id=store_id).first()

        edit_form = UpdateStoreForm(request.POST, request.FILES, instance=current_store)

        if edit_form.is_valid():
            edit_form.save(commit=True)

            return redirect('show-store')

        context = {
            'edit_form': edit_form,
        }

        return render(request, 'Store/update-store.html', context)
