from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PPST.models import Test, Doctor, Notification, Stimuli_Response

# Install fixture
doctor = [Doctor.objects.create_user(username= "Doctor. " + str(i)) for i in range(0,10)]
for d in doctor:
    d.save()


# Task status 0 = not started, 1 = in progress, 2 = completed
t0 = Test(test_id="201", age=68, assignee=doctor[0], status=0)
t0.save()
t1 = Test(test_id="303", age=75, assignee=doctor[3], status=0)
t1.save()
t2 = Test(test_id="404", age=54, assignee=doctor[2], status=1)
t2.save()
t3 = Test(test_id="505", age=82, assignee=doctor[5], status=0)
t3.save()
t4 = Test(test_id="606", age=60, assignee=doctor[4], status=1)
t4.save()
t5 = Test(test_id="707", age=90, assignee=doctor[6], status=0)
t5.save()
t6 = Test(test_id="808", age=67, assignee=doctor[1], status=1)
t6.save()
t7 = Test(test_id="909", age=55, assignee=doctor[4], status=1)
t7.save()
t8 = Test(test_id="1010", age=80, assignee=doctor[8], status=1)
t8.save()
t9 = Test(test_id="1111", age=62, assignee=doctor[7], status=0)
t9.save()
t10 = Test(test_id="1212", age=79, assignee=doctor[10], status=0)
t10.save()


s0 = Stimuli_Response(test="101", response="12334", enum_type=2, response_time="100 seconds", response_per_click="3 seconds")
s0.save()

s1 = Stimuli_Response(test="202", response="5678", enum_type=1, response_time="150 seconds", response_per_click="4 seconds")
s1.save()

s2 = Stimuli_Response(test="303", response="9A7H", enum_type=3, response_time="200 seconds", response_per_click="5 seconds")
s2.save()

s3 = Stimuli_Response(test="404", response="43821", enum_type=2, response_time="120 seconds", response_per_click="2 seconds")
s3.save()

s4 = Stimuli_Response(test="505", response="8765", enum_type=1, response_time="90 seconds", response_per_click="4 seconds")
s4.save()

s5 = Stimuli_Response(test="606", response="24AH", enum_type=3, response_time="180 seconds", response_per_click="6 seconds")
s5.save()

s6 = Stimuli_Response(test="707", response="13957", enum_type=2, response_time="110 seconds", response_per_click="3 seconds")
s6.save()

s7 = Stimuli_Response(test="808", response="3579", enum_type=1, response_time="130 seconds", response_per_click="5 seconds")
s7.save()

s8 = Stimuli_Response(test="909", response="86B2", enum_type=3, response_time="160 seconds", response_per_click="4 seconds")
s8.save()

s9 = Stimuli_Response(test="1010", response="13569", enum_type=2, response_time="140 seconds", response_per_click="3 seconds")
s9.save()

s10 = Stimuli_Response(test="1111", response="9875", enum_type=1, response_time="200 seconds", response_per_click="2 seconds")
s10.save()


n1 = Notification(message="Your patient has taken their test!")
n1.save()
n1.users.add(doctor[0], doctor[3])

n2 = Notification(message="Your Patient has started their test!")
n2.save()
n2.users.add(doctor[4])

n3 = Notification(message="Your patient has recivied their test!")
n3.save()
n3.users.add(doctor[1])
