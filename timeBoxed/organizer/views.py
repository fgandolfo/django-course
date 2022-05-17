from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .constants import MONTH_ORGANIZER
from django.urls import reverse

def index(request):

    render_dict = {
        'month_list': list(MONTH_ORGANIZER.keys())
    }
    return render(request, "organizer/index.html", render_dict)

def monthly_organizer_by_int(request, month):
    months = list(MONTH_ORGANIZER.keys())

    try:
        redirect_month = months[month-1]

    except IndexError:
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_path = reverse("month-organizer", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_organizer(request, month):

    value_by_month = MONTH_ORGANIZER.get(month, False)

    if value_by_month is False: return HttpResponseNotFound("<h1>Month not supported</h1>")

    render_dict = {
        'text': value_by_month,
        'month': month,
        'index_link': reverse("index")
    }
    return render(request, "organizer/organizer.html", render_dict)