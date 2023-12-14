from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .models import Store
from .forms import StoreRegisterForm
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .forms import UpdateStoreForm, FilterStoreForm
from django.db.models import Q


@login_required
def show_store(request):

    filter_store = FilterStoreForm(request.POST)

    stores = Store.objects.all()
    found_stores = Store.objects.filter(is_delete=False)

    context = {
        'stores': stores,
        'found_stores': found_stores,
        'filterStoreForm': filter_store,
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


@login_required
def delete_store(request, store_id):
    store = Store.objects.filter(id=store_id).first()
    store.is_delete = True
    store.save()

    return redirect('show-store')


@method_decorator(login_required, name='dispatch')
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


@login_required
def filter_stores(request: HttpRequest):
    is_filter = True

    filter_store = FilterStoreForm(request.POST)
    stores = Store.objects.all()

    if filter_store.is_valid():
        store_name = filter_store.cleaned_data.get('store_name')

        found_stores = Store.objects.filter(
            Q(is_delete=False),
            Q(id=store_name) if store_name else Q(),
        )

        context = {
            'filterStoreForm': filter_store,
            'stores': stores,
            'is_filter': is_filter,
            'found_stores': found_stores,
        }

        return render(request, 'Store/show-stores.html', context)
