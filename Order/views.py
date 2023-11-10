from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from .models import Order
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
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
            store = register_form.cleaned_data.get('store_name')
            order_number = register_form.cleaned_data.get('order_number')
            shipping_method = register_form.cleaned_data.get('shipping_method')
            description = register_form.cleaned_data.get('description')

            print(store)
            print(order_number)
            print(shipping_method)
            print(description)

            new_doc = Order(
                store_id=store,
                order_number=order_number,
                shipping_method=shipping_method,
                description=description,
            )

            new_doc.save()

            return redirect('show-store')

        # context = {
        #     'register_form': register_form,
        # }
        #
        # return render(request, 'Store/add-store.html', context)