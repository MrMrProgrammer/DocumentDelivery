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

    order_number = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره سفارش',
            'autocomplete': "off",
        })
    )

    document_defects = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نقص مدارک',
            'autocomplete': "off",
        })
    )

    shipping_method = forms.ModelChoiceField(
        queryset=ShippingMethod.objects.all(),
        empty_label="روش ارسال",
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
    )

    date = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تاریخ',
            'data-jdp': 'data-jdp',
            'autocomplete': "off",
        })
    )

    time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'ساعت',
            'autocomplete': "off",
            'type': 'time',
        }),
    )


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = ['store', 'order_number', 'document_defects', 'shipping_method', 'date', 'time']
        fields = ['order_number', 'document_defects', 'shipping_method']

        widgets = {
            'order_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره سفارش'
            }),

            'document_defects': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نقص مدارک',
            }),

            'shipping_method': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'روش ارسال',
                'required': True,
            }),
            #
            #
            # 'date': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'تاریخ',
            #     'data-jdp': 'data-jdp',
            #     'autocomplete': "off",
            # }),
            #
            # 'time': forms.TimeInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'ساعت',
            # }),

        }
        #
        # labels = {
        #     'order_number': 'شماره سفارش',
        #     'document_defects': 'نقص مدارک',
        #     'shipping_method': 'روش ارسال',
        # }


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
        }))

    from_date = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'از تاریخ',
            'data-jdp': 'data-jdp',
            "autocomplete": "off",
        }))

    to_date = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تا تاریخ',
            'data-jdp': 'data-jdp',
            "autocomplete": "off",
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
