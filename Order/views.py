from django.shortcuts import render
from django.views import View
from .forms import OrderForm


# Create your views here.

class GetDocument(View):

    def get(self, request):
        register_form = OrderForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'Order/get-document.html', context)

    def post(self, request):

        register_form = OrderForm(request.POST)

        if register_form.is_valid():

            store = register_form.cleaned_data.get('store')

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
