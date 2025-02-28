from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Given_Stimuli(models.Model):
    given_stimuli = models.TextField()
    options_stimuli = models.TextField()
    enum_type = models.TextField()

class Stimuli_Response(models.Model):
	enum_type = models.TextField()
	response = models.TextField()
	repsonse_time = models.FloatField()
	response_per_click = models.IntegerField()

class Test(models.Model):
    test_id = models.TextField()
    stimuli = models.OneToMany(Given_Stimuli)
    responses = models.OneToMany(Stimuli_Response)
    # patient = models.ForeignKey(Patient)
    time_started = models.DateTimeField(auto_now_add = True)
    time_ended = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(default = 0)  # 0 = not taken
    patient_age = models.IntegerField()

class Doctor(User):
	assigned_tests = models.ArrayField(models. TextField())
	# Implements Django’s User Class

class Notification(models.Model):
	status = models.IntegerField
	message = models.TextField()
	users = models.ManyToManyField(Doctor)
	Model.objects.filter(assigned_tests__contains=['doctors_username'])