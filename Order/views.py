from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from .models import Order
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from Store.models import Store
from django.http import HttpRequest, HttpResponse


def list_cleaner(input_list):
    output = []

    for i in input_list:
        output.append(i.strip())

    return output


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

            order_number_list = []
            order_number_list = order_number.split('/')

            clean_order_number_list = list_cleaner(order_number_list)

            for order in clean_order_number_list:

                if order.isdigit():

                    new_doc = Order(
                        store_id=store,
                        order_number=order,
                        shipping_method=shipping_method,
                        # description=description,
                    )

                    new_doc.save()

                elif '-' in order:
                    data = order.split('-')
                    if data[0].isdigit():
                        new_doc = Order(
                            store_id=store,
                            order_number=data[0],
                            shipping_method=shipping_method,
                            document_defects=data[1]
                        )

                        new_doc.save()

                else:
                    new_doc = Order(
                        store_id=store,
                        shipping_method=shipping_method,
                        document_defects=order
                    )

                    new_doc.save()

            # new_doc = Order(
            #     store_id=store,
            #     order_number=order_number,
            #     shipping_method=shipping_method,
            #     description=description,
            # )

            # new_doc.save()

            return redirect('show-orders')

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


def update_order(request, order_id):
    pass


def delete_order(request: HttpRequest, order_id):
    order_obj = Order.objects.filter(id=order_id).delete()
    return redirect('show-orders')
