from django.utils import timezone
from django.contrib.auth.models import User
from PPST.models import Test, Doctor, Notification, Stimuli_Response, Given_Stimuli

# Clear previous data
for model in [Doctor, Test, Given_Stimuli, Stimuli_Response, Notification]:
    model.objects.all().delete()

# Create Doctors
doctors = [Doctor.objects.create_user(username=f"Dr. {i}") for i in range(10)]
for doctor in doctors:
    doctor.save()

# Create Test Data
tests = [
    Test(test_id="301", patient_age=65, doctor=doctors[0], status=1, time_ended=timezone.now()),
    Test(test_id="402", patient_age=70, doctor=doctors[2], status=0, time_ended=timezone.now()),
    Test(test_id="503", patient_age=58, doctor=doctors[4], status=1, time_ended=timezone.now()),
    Test(test_id="604", patient_age=80, doctor=doctors[6], status=0, time_ended=timezone.now()),
]

for test in tests:
    test.save()

# Create Given Stimuli Data
gs1 = Given_Stimuli(given_stimuli="4872", enum_type="0", test=tests[0])
gs2 = Given_Stimuli(given_stimuli="KXJL", enum_type="1", test=tests[1])
gs3 = Given_Stimuli(given_stimuli="FN8R", enum_type="0", test=tests[2])
gs4 = Given_Stimuli(given_stimuli="X7H8", enum_type="1", test=tests[3])

gs1.save()
gs2.save()
gs3.save()
gs4.save()

# Create Stimuli Response Data
stimuli_responses = [
    Stimuli_Response(test=tests[0], response="4872", enum_type="2", response_time=120.5, response_per_click=3),
    Stimuli_Response(test=tests[1], response="KXJL", enum_type="1", response_time=95.3, response_per_click=4),
    Stimuli_Response(test=tests[2], response="FN8R", enum_type="3", response_time=110.7, response_per_click=2),
    Stimuli_Response(test=tests[3], response="X7M8", enum_type="2", response_time=130.2, response_per_click=5),
]

for sr in stimuli_responses:
    sr.save()

# Create Notification Data
notif1 = Notification.objects.create(message="A new test has been assigned!", status=1)
notif1.users.add(doctors[0], doctors[2])

notif2 = Notification.objects.create(message="A test result is ready!", status=0)
notif2.users.add(doctors[4], doctors[6])
