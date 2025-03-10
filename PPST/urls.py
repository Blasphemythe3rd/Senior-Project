from django.urls import path
from . import views

app_name="PPST"

urlpatterns = [
    path("test/", views.test, name="test"),
    
    path("testInfo/", views.testInfo, name="testInfo"),
    path("download_test/<str:test_id>/", views.download_test, name="download_test"),
]