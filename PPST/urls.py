from django.urls import path
from . import views

app_name = "PPST"

urlpatterns = [
    path("test/", views.test, name="test"),
    path("createtest/", views.createTest, name="createTest"), 
    path("ppstcreate/", views.ppstCreate, name="ppstCreate"),
    path("test/<str:testId>", views.test, name="test"),
]
