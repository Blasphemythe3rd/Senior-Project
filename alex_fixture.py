from django.utils import timezone
from django.contrib.auth.models import User
from PPST.models import Test, Doctor, Notification, Stimuli_Response, Given_Stimuli

# Create Doctors
doctors = [Doctor.objects.create_user(username=f"(A) Doctor {i}") for i in range(10)]
for doc in doctors:
    doc.save()

# Create Test Data
tests = [
    Test(test_id="201", patient_age=68, doctor=doctors[0], status=0, time_ended=timezone.now()),
    Test(test_id="303", patient_age=75, doctor=doctors[3], status=0, time_ended=timezone.now()),
    Test(test_id="404", patient_age=54, doctor=doctors[2], status=1, time_ended=timezone.now()),
    Test(test_id="505", patient_age=82, doctor=doctors[5], status=0, time_ended=timezone.now()),
    Test(test_id="606", patient_age=60, doctor=doctors[4], status=1, time_ended=timezone.now()),
    Test(test_id="707", patient_age=90, doctor=doctors[6], status=0, time_ended=timezone.now()),
    Test(test_id="808", patient_age=67, doctor=doctors[1], status=1, time_ended=timezone.now()),
    Test(test_id="909", patient_age=55, doctor=doctors[4], status=1, time_ended=timezone.now()),
    Test(test_id="1010", patient_age=80, doctor=doctors[8], status=1, time_ended=timezone.now()),
    Test(test_id="1111", patient_age=62, doctor=doctors[7], status=0, time_ended=timezone.now()),
]

for t in tests:
    t.save()


# Create Given_stimuli Data
gs86 = Given_Stimuli(given_stimuli = "5832", enum_type = "0", test = t[0])
gs19.save()
gs32 = Given_Stimuli(given_stimuli = "32484", enum_type = "1", test = t[2])
gs50.save()
gs23 = Given_Stimuli(given_stimuli = "NGHK", enum_type = "2", test = t[4])
gs40.save()

# Create Stimuli_Response Data
stimuli_responses = [
    Stimuli_Response(test=tests[0], response="12334", enum_type="2", response_time=100.0, response_per_click=3),
    Stimuli_Response(test=tests[1], response="5678", enum_type="1", response_time=150.0, response_per_click=4),
    Stimuli_Response(test=tests[2], response="9A7H", enum_type="3", response_time=200.0, response_per_click=5),
    Stimuli_Response(test=tests[3], response="43821", enum_type="2", response_time=120.0, response_per_click=2),
    Stimuli_Response(test=tests[4], response="8765", enum_type="1", response_time=90.0, response_per_click=4),
    Stimuli_Response(test=tests[5], response="24AH", enum_type="3", response_time=180.0, response_per_click=6),
    Stimuli_Response(test=tests[6], response="13957", enum_type="2", response_time=110.0, response_per_click=3),
    Stimuli_Response(test=tests[7], response="3579", enum_type="1", response_time=130.0, response_per_click=5),
    Stimuli_Response(test=tests[8], response="86B2", enum_type="3", response_time=160.0, response_per_click=4),
    Stimuli_Response(test=tests[9], response="13569", enum_type="2", response_time=140.0, response_per_click=3),
]

for s in stimuli_responses:
    s.save()

# Create Notification Data
n1 = Notification.objects.create(message="Your patient has taken their test!", status=1)
n1.users.add(doctors[0], doctors[3])

n2 = Notification.objects.create(message="Your patient has started their test!", status=1)
n2.users.add(doctors[4])

n3 = Notification.objects.create(message="Your patient has received their test!", status=1)
n3.users.add(doctors[1])
