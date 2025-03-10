from django.urls import path
from . import views

urlpatterns = [
    path('practice_test/', views.practiceTest, name="practiceTest"),    
    path('testScreen/', views.testScreen, name="testScreen"),    
]