from django.urls import path
from . import views

app_name="PPST"

urlpatterns = [
    path("test_page/", views.test_page, name="test_page"),
]