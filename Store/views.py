from django.shortcuts import render
from django.views import View
from .models import Store
from .forms import StoreRegisterForm


def show_store(request):
    stores = Store.objects.all()

    context = {
        'stores': stores,
    }

    return render(request, 'Store/show-stores.html', context)


class StoreRegisterView(View):

    def get(self, request):
        register_form = StoreRegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'Store/add-store.html', context)

    # def post(self, request):
    #
    #     success_message = 'رمز عبور موقت به آدرس ایمیل شما فرستاده شد.'
    #
    #     register_form = MomRegisterForm(request.POST)
    #
    #     if register_form.is_valid():
    #         mom_email = register_form.cleaned_data.get('email')
    #         mom: bool = User.objects.filter(email__iexact=mom_email).exists()
    #
    #         if mom:
    #             register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
    #
    #         else:
    #             # email_active_code = str(random.randint(10000000, 99999999))
    #             email_active_code = '13101380'
    #             first_name = register_form.cleaned_data.get('first_name')
    #             last_name = register_form.cleaned_data.get('last_name')
    #             phone_number = register_form.cleaned_data.get('phone_number')
    #             address = register_form.cleaned_data.get('address')
    #
    #             new_mom = User(is_mom=True,
    #                            email=mom_email,
    #                            first_name=first_name,
    #                            last_name=last_name,
    #                            phone_number=phone_number,
    #                            username=mom_email,
    #                            email_active_code=email_active_code,
    #                            address=address)
    #
    #             new_mom.set_password(email_active_code)
    #
    #             send_email("رمز عبور موقت", mom_email, {'email_active_code': email_active_code},
    #                        "SendMail/RegisterMail.html")
    #             new_mom.save()
    #
    #             mom_id = new_mom.id
    #
    #             new_mom_model = MomsModel(
    #                 user_id=mom_id
    #             )
    #
    #             new_mom_model.save()
    #
    #             context = {
    #                 'success_message': success_message
    #             }
    #
    #             return render(request, 'Moms/RegisterEmailSent.html', context)
    #
    #     context = {
    #         'register_form': register_form,
    #     }
    #
    #     return render(request, 'Moms/MomsRegiater.html', context)
