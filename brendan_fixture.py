from django.utils import timezone
from django.contrib.auth.models import User
from PPST.models import Test, Doctor, Notification, Stimuli_Response, Given_Stimuli

# Delete existing data
for model in [Doctor, Test, Given_Stimuli, Stimuli_Response, Notification]:
    model.objects.all().delete()

# Create new doctors
doctors = [Doctor.objects.create_user(username=f"Dr. Expert {i}") for i in range(1, 11)]
for doctor in doctors:
    doctor.save()

# Create test cases
tests = [
    Test(test_id="501", patient_age=58, doctor=doctors[2], status=1, time_ended=timezone.now()),
    Test(test_id="602", patient_age=70, doctor=doctors[4], status=0, time_ended=timezone.now()),
    Test(test_id="703", patient_age=65, doctor=doctors[6], status=1, time_ended=timezone.now()),
    Test(test_id="804", patient_age=78, doctor=doctors[8], status=0, time_ended=timezone.now()),
]

for test in tests:
    test.save()

# Assign given stimuli
gs1 = Given_Stimuli(given_stimuli="X1Y2", enum_type="0", test=tests[0])
gs2 = Given_Stimuli(given_stimuli="LMNO", enum_type="1", test=tests[1])
gs3 = Given_Stimuli(given_stimuli="P4QR", enum_type="0", test=tests[2])
gs4 = Given_Stimuli(given_stimuli="V8W7", enum_type="1", test=tests[3])

gs1.save()
gs2.save()
gs3.save()
gs4.save()

# Assign stimuli responses
stimuli_responses = [
    Stimuli_Response(test=tests[0], response="X1Y2", enum_type="2", response_time=105.3, response_per_click=3),
    Stimuli_Response(test=tests[1], response="LMNO", enum_type="1", response_time=92.6, response_per_click=4),
    Stimuli_Response(test=tests[2], response="P4QR", enum_type="3", response_time=117.2, response_per_click=2),
    Stimuli_Response(test=tests[3], response="V8W7", enum_type="2", response_time=129.4, response_per_click=5),
]

for sr in stimuli_responses:
    sr.save()

# Create notifications
notif1 = Notification.objects.create(message="Urgent: New test requires analysis!", status=1)
notif1.users.add(doctors[2], doctors[4])

notif2 = Notification.objects.create(message="Patient test results are now available.", status=0)
notif2.users.add(doctors[6], doctors[8])
