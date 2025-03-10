from django.urls import path
from . import views

app_name="PPST"

urlpatterns = [
    path("test/", views.test, name="test"),
    path("doctorHomePage/<str:username>/", views.doctorHomePage, name="doctorHomePage"),
]