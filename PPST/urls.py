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
    path('practice_test/', views.practiceTest, name="practiceTest"),    
    path('testScreen/', views.testScreen, name="testScreen"),    
    path("admin/", views.admin_page, name="admin"),  
    path("admin/list_doctors/", views.list_doctors, name="list_doctors"),
    path("admin/add_doctor/", views.add_doctor, name="add_doctor"),
    path('admin/doctor_tests/<int:doctor_id>/', views.doctor_tests, name='doctor_tests'),
    path('admin/test_details/<int:test_id>/', views.fetch_test_details, name='fetch_test_details'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('doctorHomepage/', views.doctorHomepage, name="doctorHomepage"),
]
