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
            'required':'required',
            'rows':3,
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
    is_active = forms.BooleanField(required=False, label='فعال / غیرفعال')
    food_photo = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Order
        fields = ['food_photo', 'food_name', 'food_price', 'food_recipe', 'is_active']

        widgets = {

            'food_name': forms.TextInput(attrs={
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

        labels = {
            'food_name': 'نام غذا',
            'food_price': 'قیمت',
            'food_recipe': 'دستورپخت',
            'is_active': 'فعال / غیرفعال',
            'food_photo': 'عکس غذا'
        }