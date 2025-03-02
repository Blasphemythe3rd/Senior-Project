from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PPST.models import Test, Doctor, Notification, Stimuli_Response, Given_Stimuli
import random
import string

for model in [Doctor, Test, Given_Stimuli, Stimuli_Response, Notification]:
    model.objects.all().delete()

# create 10 doctors with temporary names
doctors = [Doctor.objects.create_user(username= "Doctor. " + str(i)) for i in range(0,10)]
for doctor in doctors:
    doctor.save()

t0 = Test(test_id="101", patient_age = 68, time_started = "2025-03-01 15:30:45.123456+05:30", 
          time_ended = "2025-03-01 15:30:45.123456+05:30", status = 0, doctor = doctors[0])
t0.save()

# Stimuli for test t0
gs0_t0 = Given_Stimuli(given_stimuli="4932", enum_type="4digit_practice", test=t0)
gs0_t0.save()
gs1_t0 = Given_Stimuli(given_stimuli="0587", enum_type="4digit", test=t0)
gs1_t0.save()
gs2_t0 = Given_Stimuli(given_stimuli="6174", enum_type="4digit", test=t0)
gs2_t0.save()
gs3_t0 = Given_Stimuli(given_stimuli="3291", enum_type="4digit", test=t0)
gs3_t0.save()
gs4_t0 = Given_Stimuli(given_stimuli="70182", enum_type="5digit", test=t0)
gs4_t0.save()
gs5_t0 = Given_Stimuli(given_stimuli="93645", enum_type="5digit", test=t0)
gs5_t0.save()
gs6_t0 = Given_Stimuli(given_stimuli="28437", enum_type="5digit", test=t0)
gs6_t0.save()
gs7_t0 = Given_Stimuli(given_stimuli="d7a2", enum_type="4mixed_practice", test=t0)
gs7_t0.save()
gs8_t0 = Given_Stimuli(given_stimuli="b5g9", enum_type="4mixed", test=t0)
gs8_t0.save()
gs9_t0 = Given_Stimuli(given_stimuli="fc81", enum_type="4mixed", test=t0)
gs9_t0.save()
gs10_t0 = Given_Stimuli(given_stimuli="3d6e", enum_type="4mixed", test=t0)
gs10_t0.save()
gs11_t0 = Given_Stimuli(given_stimuli="927gd", enum_type="5mixed", test=t0)
gs11_t0.save()
gs12_t0 = Given_Stimuli(given_stimuli="f4e2c7", enum_type="5mixed", test=t0)
gs12_t0.save()
gs13_t0 = Given_Stimuli(given_stimuli="a8d3b", enum_type="5mixed", test=t0)
gs13_t0.save()

t1 = Test(test_id="102", patient_age = 72, time_started = "2025-03-02 12:14:45.123456+05:30", 
          time_ended = "2025-03-02 12:53:18.123456+05:30", status = 1, doctor = doctors[1])
t1.save()

# Stimuli for test t1
gs0_t1 = Given_Stimuli(given_stimuli="4932", enum_type="4digit_practice", test=t1)
gs0_t1.save()
gs1_t1 = Given_Stimuli(given_stimuli="0587", enum_type="4digit", test=t1)
gs1_t1.save()
gs2_t1 = Given_Stimuli(given_stimuli="6174", enum_type="4digit", test=t1)
gs2_t1.save()
gs3_t1 = Given_Stimuli(given_stimuli="3291", enum_type="4digit", test=t1)
gs3_t1.save()
gs4_t1 = Given_Stimuli(given_stimuli="70182", enum_type="5digit", test=t1)
gs4_t1.save()
gs5_t1 = Given_Stimuli(given_stimuli="93645", enum_type="5digit", test=t1)
gs5_t1.save()
gs6_t1 = Given_Stimuli(given_stimuli="28437", enum_type="5digit", test=t1)
gs6_t1.save()
gs7_t1 = Given_Stimuli(given_stimuli="d7a2", enum_type="4mixed_practice", test=t1)
gs7_t1.save()
gs8_t1 = Given_Stimuli(given_stimuli="b5g9", enum_type="4mixed", test=t1)
gs8_t1.save()
gs9_t1 = Given_Stimuli(given_stimuli="fc81", enum_type="4mixed", test=t1)
gs9_t1.save()
gs10_t1 = Given_Stimuli(given_stimuli="3d6e", enum_type="4mixed", test=t1)
gs10_t1.save()
gs11_t1 = Given_Stimuli(given_stimuli="927gd", enum_type="5mixed", test=t1)
gs11_t1.save()
gs12_t1 = Given_Stimuli(given_stimuli="f4e2c7", enum_type="5mixed", test=t1)
gs12_t1.save()
gs13_t1 = Given_Stimuli(given_stimuli="a8d3b", enum_type="5mixed", test=t1)
gs13_t1.save()

t2 = Test(test_id="103", patient_age = 88, time_started = "2025-03-02 10:10:10.123456+05:30", 
          time_ended = "2025-03-02 11:02:13.123456+05:30", status = 1, doctor = doctors[2])
t1.save()

# Stimuli for test t2
gs0_t2 = Given_Stimuli(given_stimuli="4932", enum_type="4digit_practice", test=t2)
gs0_t2.save()
gs1_t2 = Given_Stimuli(given_stimuli="0587", enum_type="4digit", test=t2)
gs1_t2.save()
gs2_t2 = Given_Stimuli(given_stimuli="6174", enum_type="4digit", test=t2)
gs2_t2.save()
gs3_t2 = Given_Stimuli(given_stimuli="3291", enum_type="4digit", test=t2)
gs3_t2.save()
gs4_t2 = Given_Stimuli(given_stimuli="70182", enum_type="5digit", test=t2)
gs4_t2.save()
gs5_t2 = Given_Stimuli(given_stimuli="93645", enum_type="5digit", test=t2)
gs5_t2.save()


# Stimuli Responses for test t0
sr0_t0 = Stimuli_Response(enum_type="0", response="a7d2", response_time=39.57, response_per_click=4, test=t0)
sr0_t0.save()
sr1_t0 = Stimuli_Response(enum_type="1", response="f5c8", response_time=21.36, response_per_click=2, test=t0)
sr1_t0.save()
sr2_t0 = Stimuli_Response(enum_type="0", response="g9b3", response_time=17.89, response_per_click=3, test=t0)
sr2_t0.save()
sr3_t0 = Stimuli_Response(enum_type="1", response="d6e1", response_time=48.14, response_per_click=5, test=t0)
sr3_t0.save()
sr4_t0 = Stimuli_Response(enum_type="0", response="c2f7b", response_time=10.25, response_per_click=1, test=t0)
sr4_t0.save()
sr5_t0 = Stimuli_Response(enum_type="1", response="b8g4d", response_time=32.71, response_per_click=3, test=t0)
sr5_t0.save()


# Stimuli responses for test t1

sr0_t1 = Stimuli_Response(enum_type="0", response="a6f3", response_time=40.26, response_per_click=3, test=t1)
sr0_t1.save()
sr1_t1 = Stimuli_Response(enum_type="1", response="d9b7", response_time=22.11, response_per_click=2, test=t1)
sr1_t1.save()
sr2_t1 = Stimuli_Response(enum_type="0", response="g5c8", response_time=18.75, response_per_click=4, test=t1)
sr2_t1.save()
sr3_t1 = Stimuli_Response(enum_type="1", response="e1d4", response_time=45.89, response_per_click=5, test=t1)
sr3_t1.save()
sr4_t1 = Stimuli_Response(enum_type="0", response="c7f2b", response_time=12.34, response_per_click=1, test=t1)
sr4_t1.save()
sr5_t1 = Stimuli_Response(enum_type="1", response="b8g3d", response_time=33.55, response_per_click=3, test=t1)
sr5_t1.save()


# Stimuli responses for test t2
sr0_t2 = Stimuli_Response(enum_type="0", response="a6f3", response_time=40.26, response_per_click=3, test=t2)
sr0_t2.save()
sr1_t2 = Stimuli_Response(enum_type="1", response="d9b7", response_time=22.11, response_per_click=2, test=t2)
sr1_t2.save()
sr2_t2 = Stimuli_Response(enum_type="0", response="g5c8", response_time=18.75, response_per_click=4, test=t2)
sr2_t2.save()
sr3_t2 = Stimuli_Response(enum_type="1", response="e1d4", response_time=45.89, response_per_click=5, test=t2)
sr3_t2.save()
sr4_t2 = Stimuli_Response(enum_type="0", response="c7f2b", response_time=12.34, response_per_click=1, test=t2)
sr4_t2.save()
sr5_t2 = Stimuli_Response(enum_type="1", response="b8g3d", response_time=33.55, response_per_click=3, test=t2)
sr5_t2.save()

notif1 = Notification.objects.create(message="A new test has been assigned!", status=1)
notif1.users.add(doctors[0], doctors[2])

notif2 = Notification.objects.create(message="A test result is ready!", status=0)
notif2.users.add(doctors[4], doctors[6])
