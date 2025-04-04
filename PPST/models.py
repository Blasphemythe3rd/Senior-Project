from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone

# Create your models here.

class Doctor(User): 	# Implements Django’s User Class
    def __str__(self):
        return f"Doctor {self.last_name}"
    
def generate_test_id(): # this generates the random test id
    while True:
        test_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) # 8 characters long I may change this, I am also considering on trying to make this more secure
        if not Test.objects.filter(test_id=test_id).exists(): #check if the test id already exists
            return test_id

class Test(models.Model): 
    #should we add a date assigned? 
    test_id = models.CharField(max_length=8, unique=True, default=generate_test_id) #default is needed it also has a unique constraint
    time_started = models.DateTimeField(null=True, blank=True) 
    time_ended = models.DateTimeField(null=True, blank=True) # had to give null and blank to have it work 
    status = models.IntegerField(default = 0) # 0 = not taken
    patient_age = models.IntegerField() 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False, default=1)
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
    timestamp = models.DateTimeField(default = timezone.now)
    is_read = models.BooleanField(default = False)
    def __str__(self):
        return f"Notification:{self.message}"