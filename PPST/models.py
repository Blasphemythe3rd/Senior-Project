from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(User): 	# Implements Django’s User Class
    def __str__(self):
        return f"Doctor {self.last_name}"

class Test(models.Model):
    test_id = models.TextField()
    time_started = models.DateTimeField(auto_now_add = True)
    time_ended = models.DateTimeField()
    status = models.IntegerField(default = 0)  # 0 = not taken
    patient_age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return f"Test ID: {self.test_id}, Status: {self.status}"

class Given_Stimuli(models.Model):
    given_stimuli = models.TextField()
    correct_order = models.TextField(default="")
    enum_type = models.TextField() # change to actual enum, or set integer flags
    def __str__(self):
        return f"{self.enum_type} Given Stimulus:{self.given_stimuli}"

class Stimuli_Response(models.Model):
    enum_type = models.TextField()
    response = models.TextField()
    response_per_click = models.JSONField() #pip install psycopg2
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    given = models.ForeignKey(Given_Stimuli, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"Test {self.test.test_id}; Stimulus {self.given.given_stimuli}"

class Notification(models.Model):
    status = models.IntegerField(default = 0)
    message = models.TextField()
    users = models.ManyToManyField(Doctor)
    def __str__(self):
        return f"Notification:{self.message}"