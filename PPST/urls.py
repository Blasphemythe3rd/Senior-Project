from django.urls import path
from . import views

app_name = "PPST"

urlpatterns = [
    path("test/", views.test, name="test"),
    path("createtest/", views.createTest, name="createTest"), 
    path("ppstcreate/", views.ppstCreate, name="ppstCreate"),
    path("test/<str:testId>", views.test, name="test"),
    path('login/', views.doctor_login, name='doctor_login'),
    path("testInfo/", views.testInfo, name="testInfo"),
    path("download_test/<str:test_id>/", views.download_test, name="download_test"),
    path('next/', views.next_page, name="next_page"),    
    path('testScreen/', views.testScreen, name="testScreen"), 
    
    ## Final Url-Path for Patients
    path('<str:testId>/', views.testScreen, name="patientTest"),   
]
