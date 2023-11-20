from django import forms
from .models import Order


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

    shipping_methods = [
        ('post', 'پست'),
        ('tipax', 'تیپاکس'),
        ('delivery', 'پیک موتوری'),
    ]

    shipping_method = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=shipping_methods,
    )

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
        fields = ['store', 'order_number', 'shipping_method', 'document_defects']

        widgets = {

            'store': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام غذا'
            }),
            'food_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'قیمت'
            }),
            'food_recipe': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'دستورپخت'
            }),

            'food_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'عکس غذا',

            }),
        }
