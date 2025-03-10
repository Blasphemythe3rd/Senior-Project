from django.urls import path
from . import views

app_name="PPST"

urlpatterns = [
    path("test/", views.test, name="test"),
    path("doctor", views.doctor, name="doctor"),
    path("average_statistics/", views.average_statistics, name="average_statistics")
]