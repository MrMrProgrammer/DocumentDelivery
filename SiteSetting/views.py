from django.shortcuts import render
import datetime


# Create your views here.

def home(request):
    date = datetime.date.today()
    print(date)

    context = {
        'date': date
    }

    return render(request, 'SiteSetting/home.html', context)
