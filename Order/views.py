# region Import Libraries

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View

from django.http import HttpResponse
from django.http import HttpRequest

from .forms import UpdateOrderForm, filterOrderForm
from .forms import OrderForm
from .models import Order

from Store.models import Store
from jalali_date import date2jalali

import datetime
import pandas as pd
import os


# endregion


def jalali_to_gregorian(jalali_date):
    from jdatetime import datetime
    jalali_datetime = datetime.strptime(jalali_date, "%Y/%m/%d").date()
    gregorian_datetime = jalali_datetime.togregorian()
    return gregorian_datetime


def list_cleaner(input_list):
    output = []

    for i in input_list:
        output.append(i.strip())

    return output


def add_new_order(store, order_number, document_defects, shipping_method, date, time):
    if store:
        new_store = store
    else:
        new_store = None

    if order_number:
        new_order_number = order_number
    else:
        new_order_number = None

    if document_defects:
        new_document_defects = document_defects
    else:
        new_document_defects = None

    if shipping_method:
        new_shipping_method = shipping_method
    else:
        new_shipping_method = None

    if date:
        new_date = date
    else:
        new_date = None

    if time:
        new_time = time
    else:
        new_time = None

    new_doc = Order(
        store_id=new_store,
        order_number=new_order_number,
        document_defects=new_document_defects,
        shipping_method=new_shipping_method,
        date=new_date,
        time=new_time,
    )
    new_doc.save()


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
            shipping_method = register_form.cleaned_data.get('shipping_method')
            date = register_form.cleaned_data.get('date')
            time = register_form.cleaned_data.get('time')

            if date == '':
                date = datetime.date.today()
            else:
                date = jalali_to_gregorian(date)

            if time is None:
                time = datetime.datetime.now()

            for i in range(1, 101):
                if i == 1:
                    order_number = request.POST.get('order_number')
                    document_defects = request.POST.get('document_defects')
                    if order_number or document_defects:
                        add_new_order(store, order_number, document_defects, shipping_method, date, time)
                        continue

                order_number = request.POST.get(f'order_number[{i}]')
                document_defects = request.POST.get(f'document_defects[{i}]')
                if order_number or document_defects:
                    add_new_order(store, order_number, document_defects, shipping_method, date, time)
                else:
                    print(i)
                    break

            return redirect('show-orders')

        context = {
            'register_form': register_form,
        }

        return render(request, 'Order/add-order.html', context)


@login_required
def show_order(request):
    is_filter = False

    orders = Order.objects.filter(is_delete=False).order_by('-id')

    orders_len = len(orders)

    stores = Store.objects.all()

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
    stores = Store.objects.all()

    if filter_order.is_valid():
        store_name = filter_order.cleaned_data.get('store_name')
        order_number = filter_order.cleaned_data['order_number']

        from_date = filter_order.cleaned_data['from_date']
        if from_date != '':
            from_date = jalali_to_gregorian(from_date)

        to_date = filter_order.cleaned_data['to_date']
        if to_date != '':
            to_date = jalali_to_gregorian(to_date)

        shipping_method = filter_order.cleaned_data['shipping_method']
        document_defects = filter_order.cleaned_data['document_defects']

        orders = Order.objects.filter(
            Q(is_delete=False),
            Q(store_id=store_name) if store_name else Q(),
            Q(order_number=order_number) if order_number else Q(),
            Q(date__gte=from_date) if from_date else Q(),
            Q(date__lte=to_date) if to_date else Q(),
            Q(shipping_method=shipping_method) if shipping_method else Q(),
            Q(document_defects__contains=document_defects) if document_defects else Q(),
        ).order_by('-id')

        orders_len = len(orders)

        context = {
            'orders': orders,
            'FilterOrderForm': filter_order,
            'stores': stores,
            'is_filter': is_filter,

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
        if from_date:
            from_date = datetime.datetime.strptime(from_date, '%Y/%m/%d')

        to_date = request.POST.get('to_date')
        if to_date:
            to_date = datetime.datetime.strptime(to_date, '%Y/%m/%d')

        shipping_method = request.POST.get('shipping_method')
        if shipping_method == 'None':
            shipping_method = None

        document_defects = request.POST.get('document_defects')

        orders = Order.objects.filter(
            Q(is_delete=False),
            Q(store_id=store_id) if store_id else Q(),
            Q(order_number=order_number) if order_number else Q(),
            Q(date__gte=from_date) if from_date else Q(),
            Q(date__lte=to_date) if to_date else Q(),
            Q(shipping_method__fa_name=shipping_method) if shipping_method else Q(),
            Q(document_defects__contains=document_defects) if document_defects else Q(),
        ).order_by('-id')

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

        excel_filename = os.path.join("Report.xlsx")

        df.to_excel(excel_filename, index=False)

        with open(excel_filename, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={excel_filename}'

        return response

    return redirect('export_to_excel')
