from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from .models import Order
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from Store.models import Store
from django.http import HttpRequest, HttpResponse
from .forms import UpdateOrderForm
from django.http import HttpResponse
import pandas as pd
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os


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

            # time = datetime. now()

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

    per_page = 10
    paginator = Paginator(orders, per_page)

    page = request.GET.get('page')

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {
        'orders': orders
    }

    return render(request, 'Order/show-orders.html', context)


@method_decorator(login_required, name='dispatch')
class UpdateOrderView(View):
    def get(self, request: HttpRequest, order_id):
        current_order: Order = Order.objects.filter(id=order_id).first()

        print(current_order.order_number)

        edit_form = UpdateOrderForm(instance=current_order)

        context = {
            'edit_form': edit_form,
            'current_order': current_order,
        }

        return render(request, 'Order/update-order.html', context)

    # def post(self, request: HttpRequest, order_id):
    #
    #     current_food: FoodsModel = FoodsModel.objects.filter(id=food_id).first()
    #
    #     edit_form = UpdateFoodForm(request.POST, request.FILES, instance=current_food)
    #
    #     if edit_form.is_valid():
    #         edit_form.save(commit=True)
    #
    #         return redirect('PerMomFoodsList')
    #
    #     context = {
    #         'edit_form': edit_form,
    #     }
    #
    #     return render(request, 'Food/UpdateFood.html', context)


def delete_order(request: HttpRequest, order_id):
    order_obj = Order.objects.filter(id=order_id).delete()
    return redirect('show-orders')


def get_report(objects):
    pass


def export_to_excel(request):

    date = datetime.now().strftime("%Y - %M - %D")

    # Your data to be exported to Excel
    data = {
        'Column1': [1, 2, 3, 4, 5, 6],
        'Column2': ['A', 'B', 'C', 'D', 'E', 'F']
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Define the path to the Report folder
    report_folder = "Report"
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)

    # Create the full path for the Excel file
    excel_filename = os.path.join(report_folder, f"Report.xlsx")

    # Export DataFrame to Excel
    df.to_excel(excel_filename, index=False)

    # Prepare response for file download
    with open(excel_filename, 'rb') as excel_file:
        response = HttpResponse(excel_file.read(),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={excel_filename}'

    return response
