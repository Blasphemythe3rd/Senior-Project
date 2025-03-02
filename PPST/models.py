from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(User): 	# Implements Django’s User Class
    #assigned_tests = models.ArrayField(Test)
    pass

class Test(models.Model):
    test_id = models.TextField()
    # stimuli = models.ForeignKey(Given_Stimuli)
    # responses = models.ForeignKey(Stimuli_Response)
    # patient = models.ForeignKey(Patient)
    time_started = models.DateTimeField(auto_now_add = True)
    time_ended = models.DateTimeField()
    status = models.IntegerField(default = 0)  # 0 = not taken
    patient_age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Given_Stimuli(models.Model):
    given_stimuli = models.TextField()
    enum_type = models.TextField() # change to actual enum, or set integer flags
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class Stimuli_Response(models.Model):
    enum_type = models.TextField()
    response = models.TextField()
    response_time = models.FloatField()
    response_per_click = models.IntegerField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class Notification(models.Model):
    status = models.IntegerField(default = 0)
    message = models.TextField()
    users = models.ManyToManyField(Doctor)
    # Model.objects.filter(assigned_tests__contains=['doctors_username'])