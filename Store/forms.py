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

    class Meta:
        model = Store
        fields = ["store_name", "is_active"]

    # is_active = forms.BooleanField(required=False, label='فعال / غیرفعال')
    # # food_photo = forms.ImageField(required=False, widget=forms.FileInput)

    # class Meta:
    #     model = Store
        # fields = ['food_photo', 'food_name', 'food_price', 'food_recipe', 'is_active']

        widgets = {

            'store_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام فروشگاه'
            }),
            #
            # 'is_active': forms.NullBooleanSelect(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'قیمت'
            # }),
        }

        labels = {
            'store_name': 'نام فروشگاه',
            'is_active': 'فعال / غیرفعال'
        }
