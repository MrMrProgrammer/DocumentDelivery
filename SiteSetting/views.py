from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from jalali_date import datetime2jalali
from datetime import datetime, timezone


# Create your views here.

@login_required
def home(request):
    date = datetime.now()
    today_date = datetime2jalali(datetime.now(timezone.utc)).strftime('%Y-%m-%d')
    print(date)

    print(today_date)

    context = {
        'today_date': today_date,
        'date': date,
    }

    return render(request, 'SiteSetting/home.html', context)
