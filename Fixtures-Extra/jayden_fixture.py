from django.utils import timezone
from django.contrib.auth.models import User
from PPST.models import Test, Doctor, Notification, Stimuli_Response, Given_Stimuli

for model in [Doctor, Test, Given_Stimuli, Stimuli_Response, Notification]:
    model.objects.all().delete()

doctors = [Doctor.objects.create_user(username=f"Dr. {i}") for i in range(10)]
for doctor in doctors:
    doctor.save()

tests = [
    Test(test_id="105", patient_age=64, doctor=doctors[1], status=1, time_ended=timezone.now()),
    Test(test_id="206", patient_age=72, doctor=doctors[3], status=0, time_ended=timezone.now()),
    Test(test_id="307", patient_age=60, doctor=doctors[5], status=1, time_ended=timezone.now()),
    Test(test_id="408", patient_age=75, doctor=doctors[7], status=0, time_ended=timezone.now()),
]

for test in tests:
    test.save()

gs1 = Given_Stimuli(given_stimuli="A3Z5", enum_type="0", test=tests[0])
gs2 = Given_Stimuli(given_stimuli="BGTY", enum_type="1", test=tests[1])
gs3 = Given_Stimuli(given_stimuli="N5QX", enum_type="0", test=tests[2])
gs4 = Given_Stimuli(given_stimuli="Z2R9", enum_type="1", test=tests[3])

gs1.save()
gs2.save()
gs3.save()
gs4.save()

stimuli_responses = [
    Stimuli_Response(test=tests[0], response="A3Z5", enum_type="2", response_time=115.5, response_per_click=3),
    Stimuli_Response(test=tests[1], response="BGTY", enum_type="1", response_time=98.4, response_per_click=4),
    Stimuli_Response(test=tests[2], response="N5QX", enum_type="3", response_time=122.7, response_per_click=2),
    Stimuli_Response(test=tests[3], response="Z2F9", enum_type="2", response_time=134.8, response_per_click=5),
]

for sr in stimuli_responses:
    sr.save()

notif1 = Notification.objects.create(message="New test assigned! Please review.", status=1)
notif1.users.add(doctors[1], doctors[3])

notif2 = Notification.objects.create(message="Test result is ready for review!", status=0)
notif2.users.add(doctors[5], doctors[7])
