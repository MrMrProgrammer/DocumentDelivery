from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from jalali_date import datetime2jalali
from datetime import datetime, timezone
from Order.models import Order


def chart_date(start_date, end_date):
    orders = Order.objects.filter(date__gte=start_date, date__lte=end_date, is_delete=False)

    yValues = [0, 0, 0, 0, 0]

    for i in orders:
        if i.date.strftime('%A') == 'Saturday':
            yValues[0] += 1
        elif i.date.strftime('%A') == 'Sunday':
            yValues[1] += 1
        elif i.date.strftime('%A') == 'Monday':
            yValues[2] += 1
        elif i.date.strftime('%A') == 'Tuesday':
            yValues[3] += 1
        elif i.date.strftime('%A') == 'Wednesday':
            yValues[4] += 1

    return yValues


@login_required
def home(request):
    date = datetime.now()
    day_of_week = date.strftime('%A')
    today_date = datetime2jalali(datetime.now(timezone.utc)).strftime('%Y-%m-%d')

    if day_of_week == 'Saturday':
        start_date = datetime.now() - timedelta(days=7)
        end_date = start_date + timedelta(days=4)

        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        yValues = chart_date(start_date, end_date)

    elif day_of_week == 'Sunday':
        start_date = datetime.now() - timedelta(days=8)
        end_date = start_date + timedelta(days=4)

        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        yValues = chart_date(start_date, end_date)

    elif day_of_week == 'Monday':
        start_date = datetime.now() - timedelta(days=9)
        end_date = start_date + timedelta(days=4)

        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        yValues = chart_date(start_date, end_date)

    elif day_of_week == 'Tuesday':
        start_date = datetime.now() - timedelta(days=10)
        end_date = start_date + timedelta(days=4)

        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        yValues = chart_date(start_date, end_date)

    elif day_of_week == 'Wednesday':
        start_date = datetime.now() - timedelta(days=11)
        end_date = start_date + timedelta(days=4)

        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        yValues = chart_date(start_date, end_date)

    elif day_of_week == 'Thursday':
        start_date = datetime.now() - timedelta(days=5)
        end_date = start_date + timedelta(days=4)

        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        yValues = chart_date(start_date, end_date)

    elif day_of_week == 'Friday':
        start_date = datetime.now() - timedelta(days=6)
        end_date = start_date + timedelta(days=4)

        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        yValues = chart_date(start_date, end_date)

    start_date = datetime2jalali().strftime('%Y-%m-%d')

    context = {
        'today_date': today_date,
        'date': date,
        'yValues': yValues,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'SiteSetting/home.html', context)