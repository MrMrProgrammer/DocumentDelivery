from django import forms
from .models import Store


class StoreRegisterForm(forms.Form):
    store_name = forms.CharField(
        label='نام فروشگاه',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'نام فروشگاه'
        }),
    )
    is_active = forms.BooleanField()


class UpdateStoreForm(forms.ModelForm):

    is_active = forms.BooleanField(required=False, label='فعال / غیرفعال')
    # food_photo = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Store
        # fields = ['food_photo', 'food_name', 'food_price', 'food_recipe', 'is_active']

        # widgets = {
        #
        #     'food_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'نام غذا'
        #     }),
        #     'food_price': forms.NumberInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'قیمت'
        #     }),
        #     'food_recipe': forms.Textarea(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'دستورپخت'
        #     }),
        #
        #     'food_photo': forms.ClearableFileInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'عکس غذا',
        #
        #     }),
        # }
        #
        # labels = {
        #     'food_name': 'نام غذا',
        #     'food_price': 'قیمت',
        #     'food_recipe': 'دستورپخت',
        #     'is_active': 'فعال / غیرفعال',
        #     'food_photo': 'عکس غذا'
        # }