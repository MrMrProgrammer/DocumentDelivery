from django.shortcuts import render
import datetime


# Create your views here.

def home(request):
    date = datetime.date.today()  # Returns 2018-01-15

    context = {
        'date': date
    }

    return render(request, 'SiteSetting/home.html', context)
