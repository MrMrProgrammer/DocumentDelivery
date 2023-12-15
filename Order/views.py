import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from .models import Order
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from Store.models import Store
from django.http import HttpRequest, HttpResponse
from .forms import UpdateOrderForm, filterOrderForm
from django.http import HttpResponse
import pandas as pd
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from jalali_date import date2jalali


def list_cleaner(input_list):
    output = []

    for i in input_list:
        output.append(i.strip())

    return output


@method_decorator(login_required, name='dispatch')
class GetDocument(View):
    def get(self, request):
        stores = Store.objects.filter(is_delete=False)

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
            date = register_form.cleaned_data.get('date')
            time = register_form.cleaned_data.get('time')

            if date == None:
                date = datetime.date.today()
            #     .strftime('%Y-%M-%D')

            if time == None:
                time = datetime.datetime.now()
            #     .strftime('%H:%M')

            order_number_list = []
            order_number_list = order_number.split('/')

            clean_order_number_list = list_cleaner(order_number_list)

            for order in clean_order_number_list:

                if order.isdigit():

                    new_doc = Order(
                        store_id=store,
                        order_number=order,
                        shipping_method=shipping_method,
                        date=date,
                        time=time,
                    )

                    new_doc.save()

                elif '-' in order:
                    data = order.split('-')

                    data = list_cleaner(data)

                    if data[0].isdigit():
                        new_doc = Order(
                            store_id=store,
                            order_number=data[0],
                            shipping_method=shipping_method,
                            date=date,
                            time=time,
                            document_defects=data[1]
                        )

                        new_doc.save()

                else:
                    new_doc = Order(
                        store_id=store,
                        shipping_method=shipping_method,
                        document_defects=order,
                        date=date,
                        time=time,
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
    is_filter = False

    orders = Order.objects.filter(is_delete=False).order_by('-id')
    orders_for_report = orders

    orders_len = len(orders)

    stores = Store.objects.filter().all()

    filter_order = filterOrderForm(request.POST)

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
        'orders': orders,
        'FilterOrderForm': filter_order,
        'stores': stores,
        'is_filter': is_filter,
        'orders_for_report': orders_for_report,

        'orders_len': orders_len,
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


@login_required
def delete_order(request: HttpRequest, order_id):
    order_obj = Order.objects.filter(id=order_id).first()
    order_obj.is_delete = True
    order_obj.save()
    return redirect('show-orders')


@login_required
def filter_orders(request: HttpRequest):
    is_filter = True

    filter_order = filterOrderForm(request.POST)
    stores = Store.objects.filter().all()

    if filter_order.is_valid():
        store_name = filter_order.cleaned_data.get('store_name')
        order_number = filter_order.cleaned_data['order_number']
        from_date = filter_order.cleaned_data['from_date']
        to_date = filter_order.cleaned_data['to_date']
        shipping_method = filter_order.cleaned_data['shipping_method']
        print(type(shipping_method))
        document_defects = filter_order.cleaned_data['document_defects']

        report_data = {
            'store_name': store_name,
            'order_number': order_number,
            'from_date': from_date,
            'to_date': to_date,
            'shipping_method': shipping_method,
            'document_defects': document_defects,
        }

        orders = Order.objects.filter(
            Q(is_delete=False),
            Q(store_id=store_name) if store_name else Q(),
            Q(order_number=order_number) if order_number else Q(),
            # Q(from_date__gte=from_date) if from_date else Q(),
            # Q(to_date__lte=to_date) if to_date else Q(),
            Q(shipping_method=shipping_method) if shipping_method else Q(),
            Q(document_defects__contains=document_defects) if document_defects else Q(),
        )

        orders_for_report = orders

        orders_len = len(orders)

        context = {
            'orders': orders,
            'FilterOrderForm': filter_order,
            'stores': stores,
            'is_filter': is_filter,
            'orders_for_report': orders_for_report,
            'report_data': report_data,

            'store_name': store_name,
            'order_number': order_number,
            'from_date': from_date,
            'to_date': to_date,
            'shipping_method': shipping_method,
            'document_defects': document_defects,

            'orders_len': orders_len,
        }

        return render(request, 'Order/show-orders.html', context)


@login_required
def export_to_excel(request: HttpRequest):
    if request.method == 'POST':

        store_id = request.POST.get('store_name')

        order_number = request.POST.get('order_number')

        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        shipping_method = request.POST.get('shipping_method')
        if shipping_method == 'None':
            shipping_method = None

        document_defects = request.POST.get('document_defects')

        orders = Order.objects.filter(
            Q(is_delete=False),
            Q(store_id=store_id) if store_id else Q(),
            Q(order_number=order_number) if order_number else Q(),
            # # Q(from_date__gte=from_date) if from_date else Q(),
            # # Q(to_date__lte=to_date) if to_date else Q(),
            Q(shipping_method__fa_name=shipping_method) if shipping_method else Q(),
            Q(document_defects__contains=document_defects) if document_defects else Q(),
        )

        print("Len : ", len(orders))

        if len(orders) == 0:
            orders = Order.objects.all()

        store_name = []
        order_number = []
        date = []
        time = []
        shipping_method = []
        document_defects = []

        for order in orders:
            store_name.append(order.store.store_name)

            order_number.append(order.order_number)

            jalali_date = date2jalali(order.date)
            date.append(jalali_date)

            st_time = order.time.strftime("%H:%M")
            time.append(st_time)

            shipping_method.append(order.shipping_method)

            document_defects.append(order.document_defects)

        df = pd.DataFrame({'نام فروشگاه': store_name,
                           'شماره سفارش': order_number,
                           'تاریخ': date,
                           'ساعت': time,
                           'روش ارسال': shipping_method,
                           'نقص مدارک': document_defects, })

        report_folder = "Report"
        if not os.path.exists(report_folder):
            os.makedirs(report_folder)

        # excel_filename = os.path.join(report_folder, f"Report.xlsx")
        excel_filename = os.path.join("Report.xlsx")

        df.to_excel(excel_filename, index=False)

        # Read the Excel file and send the response
        with open(excel_filename, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={excel_filename}'

        return response

    return redirect('export_to_excel')

    # # data = request.GET.get('data')
    #
    # data = request.GET.POST()
    #
    # print(request)
    #
    # data = {
    #     'Column1': [1, 2, 3, 4, 5, 6],
    #     'Column2': ['A', 'B', 'C', 'D', 'E', 'F']
    # }
    #
    # df = pd.DataFrame(data)
    #
    # report_folder = "Report"
    # if not os.path.exists(report_folder):
    #     os.makedirs(report_folder)
    #
    # excel_filename = os.path.join(report_folder, f"Report.xlsx")
