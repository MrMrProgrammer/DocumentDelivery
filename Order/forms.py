from django import forms
from .models import Order


# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'

class OrderForm(forms.Form):
    store_name = forms.CharField(
        label='نام فروشگاه',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'نام فروشگاه',
            'onclick': "dropfunc()",
            'id': 'myDropdownBtn',
        }),
    )

    order_number = forms.IntegerField(
        label='شماره سفارش',
        widget=forms.NumberInput(attrs=
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

    description = forms.CharField(
        label='توضیحات',
        widget=forms.Textarea(attrs=
        {
            'class': 'form-control',
            'placeholder': 'توضیحات',
            'rows': 5
        }),
    )
