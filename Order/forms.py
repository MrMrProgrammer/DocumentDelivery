from django import forms
from .models import Order, ShippingMethod


class OrderForm(forms.Form):
    store_name = forms.CharField(
        label='نام فروشگاه',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'نام فروشگاه',
            'id': 'store_id_input',
            'readonly': 'readonly',
            'type': 'hidden',
            'required': 'required',
            'rows': 3,
        }),
    )

    order_number = forms.CharField(
        label='شماره سفارش',
        required=False,
        widget=forms.Textarea(attrs=
        {
            'class': 'form-control',
            'placeholder': 'شماره سفارش'
        }),
    )

    shipping_method = forms.ModelChoiceField(
        queryset=ShippingMethod.objects.all(),
         empty_label="روش ارسال",
         widget=forms.Select(attrs={
             'class': 'form-control'
         }),
    )

    # widget=forms.RadioSelect
    # description = forms.CharField(
    #     label='توضیحات',
    #     required=False,
    #     widget=forms.Textarea(attrs=
    #     {
    #         'class': 'form-control',
    #         'placeholder': 'توضیحات',
    #         'rows': 5
    #     }),
    # )


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_number', 'shipping_method', 'document_defects', 'date', 'time']

        widgets = {
            'order_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'قیمت'
            }),
            'shipping_method': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'روش ارسال',

            }),

            'document_defects': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نقص مدارک',
            }),

            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'تاریخ',
            }),

            'time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ساعت',
            }),

        }


class filterOrderForm(forms.Form):
    store_name = forms.CharField(
        label='نام فروشگاه',
        required=False,
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'نام فروشگاه',
            'id': 'store_id_input',
            'readonly': 'readonly',
            'type': 'hidden',
            'rows': 3,
        }),
    )

    order_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره سفارش',
            'required': False
        }))

    from_date = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'از تاریخ',
        }))

    to_date = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تا تاریخ',
            'required': False
        }))

    shipping_method = forms.ModelChoiceField(
        required=False,
        queryset=ShippingMethod.objects.all(),
        empty_label="روش ارسال",
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
    )

    document_defects = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نقص مدارک',
            'required': False
        }))
