from django.urls import path
from . import views

app_name = "PPST"

urlpatterns = [
    path("test/", views.test, name="test"),
    path("createtest/", views.createTest, name="createTest"), 
    path("ppstcreate/", views.ppstCreate, name="ppstCreate"),
    path("test/<str:testId>", views.test, name="test"),
    path('login/', views.doctor_login, name='doctor_login'),
    path('logout/', views.logout_view, name='logout'),
    path("testInfo/", views.testInfo, name="testInfo"),
    path("download_test/<str:test_id>/", views.download_test, name="download_test"),
    
    ## this is the url for the test completed notification

    path("notification/", views.create_notification_test_completed, name="create_notification_test_completed"), 
    
    path('save_response/', views.save_response, name='save_response'),

    ## Final Url-Path for Patients
    path('testScreen/<str:testId>/', views.testScreen, name="testScreen"), 
    path('testStart/<str:testId>/', views.testStart, name="testStart"),
    path('settings/<str:testId>/', views.setting, name="settings"), 
    path('testComplete/', views.testComplete, name="testComplete"), 
    path("admin/", views.admin_page, name="admin"),  
    path("admin/list_doctors/", views.list_doctors, name="list_doctors"),
    path("admin/add_doctor/", views.add_doctor, name="add_doctor"),
    path('admin/doctor_tests/<int:doctor_id>/', views.doctor_tests, name='doctor_tests'),
    path('admin/test_details/<int:test_id>/', views.fetch_test_details, name='fetch_test_details'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('doctorHomePage/', views.doctorHomePage, name="doctorHomePage"),
    path("average_statistics/", views.average_statistics, name="average_statistics"),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<str:token>/', views.reset_password, name='reset_password'),
    path('reset-password-token/', views.reset_password_token, name='reset_password_token'),
    path('reset-password/', views.reset_password, name='reset_password'),

]
