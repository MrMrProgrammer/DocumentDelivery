from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from .models import Order
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from Store.models import Store


@method_decorator(login_required, name='dispatch')
class GetDocument(View):
    def get(self, request):
        stores = Store.objects.all()

        register_form = OrderForm()

        context = {
            'register_form': register_form,
            'stores': stores,
        }

        return render(request, 'Order/add-order.html', context)

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

        context = {
            'register_form': register_form,
        }

        return render(request, 'Order/add-order.html', context)


@login_required
def show_order(request):
    orders = Order.objects.all()

    context = {
        'orders': orders
    }

    return render(request, 'Order/show-orders.html', context)
