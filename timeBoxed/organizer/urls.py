from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_organizer_by_int),
    path("<str:month>", views.monthly_organizer, name="month-organizer"),
]