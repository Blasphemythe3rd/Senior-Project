from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PPST.models import Test, Doctor, Notification, Stimuli_Response, Given_Stimuli

for c in [Doctor, Test, Given_Stimuli, Stimuli_Response, Notification]:
    c.objects.all().delete()

# Install fixture
doctors = [Doctor.objects.create_user(username= "Doctor. " + str(i)) for i in range(0,10)]
for d in doctors:
    d.save()


t0 = Test(test_id="101", patient_age = 68, time_started = "2025-03-01 15:30:45.123456+05:30", 
          time_ended = "2025-03-01 15:30:45.123456+05:30", status = 0, doctor = doctors[0])
t0.save()

gs0 = Given_Stimuli(given_stimuli = "dcba", enum_type = "0", test = t0)
gs0.save()
gs1 = Given_Stimuli(given_stimuli = "hgfe", enum_type = "1", test = t0)
gs1.save()
gs2 = Given_Stimuli(given_stimuli = "mlkj", enum_type = "0", test = t0)
gs2.save()

sr0 = Stimuli_Response(enum_type = "0", response = "abcd", response_time = 10.01, response_per_click = 3, test = t0)
sr0.save()
sr1 = Stimuli_Response(enum_type = "1", response = "efgh", response_time = 50.05, response_per_click = 2, test = t0)
sr1.save()
sr2 = Stimuli_Response(enum_type = "0", response = "jklm", response_time = 3.3, response_per_click = 1, test = t0)
sr2.save()

t1 = Test(test_id="102", patient_age = 72, time_started = "2025-03-02 15:30:45.123456+05:30", 
          time_ended = "2025-03-02 15:30:45.123456+05:30", status = 1, doctor = doctors[1])
t1.save()

gs3 = Given_Stimuli(given_stimuli = "4321", enum_type = "0", test = t1)
gs3.save()
gs4 = Given_Stimuli(given_stimuli = "6540", enum_type = "1", test = t1)
gs4.save()
gs5 = Given_Stimuli(given_stimuli = "9870", enum_type = "0", test = t1)
gs5.save()

sr3 = Stimuli_Response(enum_type = "0", response = "1324", response_time = 9.4, response_per_click = 3, test = t1)
sr3.save()
sr4 = Stimuli_Response(enum_type = "1", response = "0456", response_time = 5.65, response_per_click = 2, test = t1)
sr4.save()
sr5 = Stimuli_Response(enum_type = "0", response = "0789", response_time = 12.3, response_per_click = 1, test = t1)
sr5.save()

notif1 = Notification(status = 0, message = "Test #XXXX has been submitted!")
notif1.save()
notif1.users.set(doctors) # give all doctors this notification