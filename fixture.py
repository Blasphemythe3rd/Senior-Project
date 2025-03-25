from django.db import models
from PPST.models import Doctor, Test, Given_Stimuli, Stimuli_Response, Notification

for c in [Doctor, Test, Given_Stimuli, Stimuli_Response, Notification]:
    c.objects.all().delete()

import random
import string
import datetime
from django.utils.timezone import now
#---------------------------------------------------------------------------
try:
    # creates the doctors based off the doctors_data
    d0 = Doctor(username="doctor0", email="alice.smith@hospital.com", password="SecurePass123", first_name="Alice", last_name="Smith")
    d0.save()
    d1 = Doctor(username="doctor1", email="bob.jones@hospital.com", password="SecurePass123", first_name="Bob", last_name="Jones")
    d1.save()
    d2 = Doctor(username="doctor2", email="charlie.brown@hospital.com", password="SecurePass123", first_name="Charlie", last_name="Brown")
    d2.save()
    d3 = Doctor(username="doctor3", email="diana.taylor@hospital.com", password="SecurePass123", first_name="Diana", last_name="Taylor")
    d3.save()
    d4 = Doctor(username="doctor4", email="edward.miller@hospital.com", password="SecurePass123", first_name="Edward", last_name="Miller")
    d4.save()
    d5 = Doctor(username="doctor5", email="fiona.clark@hospital.com", password="SecurePass123", first_name="Fiona", last_name="Clark")
    d5.save()

    d0 = Doctor(username="doctor0", email="alice.smith@hospital.com", password="SecurePass123", first_name="Alice", last_name="Smith")
    d0.save()
    d1 = Doctor(username="doctor1", email="bob.jones@hospital.com", password="SecurePass123", first_name="Bob", last_name="Jones")
    d1.save()
    d2 = Doctor(username="doctor2", email="charlie.brown@hospital.com", password="SecurePass123", first_name="Charlie", last_name="Brown")
    d2.save()
    d3 = Doctor(username="doctor3", email="diana.taylor@hospital.com", password="SecurePass123", first_name="Diana", last_name="Taylor")
    d3.save()
    d4 = Doctor(username="doctor4", email="edward.miller@hospital.com", password="SecurePass123", first_name="Edward", last_name="Miller")
    d4.save()
    d5 = Doctor(username="doctor5", email="fiona.clark@hospital.com", password="SecurePass123", first_name="Fiona", last_name="Clark")
    d5.save()

    doctors = list(Doctor.objects.all())
    t0 = Test(
        test_id="t0",
        time_started=now(),
        time_ended=now() + datetime.timedelta(minutes=random.randint(5, 60)),
        status=0,
        patient_age=45,
        doctor=doctors[0]
    )
    t0.save()

    t1 = Test(
        test_id="t1",
        time_started=now(),
        time_ended=now() + datetime.timedelta(minutes=random.randint(5, 60)),
        status=0,
        patient_age=55,
        doctor=doctors[1]
    )
    t1.save()
    t2 = Test(
        test_id="t2",
        time_started=now(),
        time_ended=now() + datetime.timedelta(minutes=random.randint(5, 60)),
        status=0,
        patient_age=65,
        doctor=doctors[2]
    )
    t2.save()
    t3 = Test(
        test_id="t3",
        time_started=now(),
        time_ended=now() + datetime.timedelta(minutes=random.randint(5, 60)),
        status=0,
        patient_age=75,
        doctor=doctors[3]
    )
    t3.save()
    t4 = Test(
        test_id="t4",
        time_started=now(),
        time_ended=now() + datetime.timedelta(minutes=random.randint(5, 60)),
        status=0,
        patient_age=85,
        doctor=doctors[4]
    )
    t4.save()
except Exception as e:
    print(f"Error: {e}")
#Given Stimuli creation-------------------------------------------------------------------------
# gs0 = Given_Stimuli(given_stimuli="2384", enum_type="4digit_practice")
# gs0.save()
# gs1 = Given_Stimuli(given_stimuli="4927", enum_type="4digit")
# gs1.save()
# gs2 = Given_Stimuli(given_stimuli="5736", enum_type="4digit")
# gs2.save()
# gs3 = Given_Stimuli(given_stimuli="6852", enum_type="4digit")
# gs3.save()
# gs4 = Given_Stimuli(given_stimuli="74862", enum_type="5digit")
# gs4.save()
# gs5 = Given_Stimuli(given_stimuli="35826", enum_type="5digit")
# gs5.save()
# gs6 = Given_Stimuli(given_stimuli="46715", enum_type="5digit")
# gs6.save()
# gs7 = Given_Stimuli(given_stimuli="2A3F", enum_type="4mixed_practice")
# gs7.save()
# gs8 = Given_Stimuli(given_stimuli="N54Q", enum_type="4mixed")
# gs8.save()
# gs9 = Given_Stimuli(given_stimuli="H78X", enum_type="4mixed")
# gs9.save()
# gs10 = Given_Stimuli(given_stimuli="R6Y2", enum_type="4mixed")
# gs10.save()
# gs11 = Given_Stimuli(given_stimuli="3Q4AF", enum_type="5mixed")
# gs11.save()
# gs12 = Given_Stimuli(given_stimuli="2RHN6", enum_type="5mixed")
# gs12.save()
# gs13 = Given_Stimuli(given_stimuli="N85QR", enum_type="5mixed")
# gs13.save()
gs0 = Given_Stimuli(given_stimuli="2384", correct_order="2348", enum_type="4digit_practice")
#Given Stimuli creation-------------------------------------------------------------------------
# gs0 = Given_Stimuli(given_stimuli="2384", enum_type="4digit_practice")
# gs0.save()
# gs1 = Given_Stimuli(given_stimuli="4927", enum_type="4digit")
# gs1.save()
# gs2 = Given_Stimuli(given_stimuli="5736", enum_type="4digit")
# gs2.save()
# gs3 = Given_Stimuli(given_stimuli="6852", enum_type="4digit")
# gs3.save()
# gs4 = Given_Stimuli(given_stimuli="74862", enum_type="5digit")
# gs4.save()
# gs5 = Given_Stimuli(given_stimuli="35826", enum_type="5digit")
# gs5.save()
# gs6 = Given_Stimuli(given_stimuli="46715", enum_type="5digit")
# gs6.save()
# gs7 = Given_Stimuli(given_stimuli="2A3F", enum_type="4mixed_practice")
# gs7.save()
# gs8 = Given_Stimuli(given_stimuli="N54Q", enum_type="4mixed")
# gs8.save()
# gs9 = Given_Stimuli(given_stimuli="H78X", enum_type="4mixed")
# gs9.save()
# gs10 = Given_Stimuli(given_stimuli="R6Y2", enum_type="4mixed")
# gs10.save()
# gs11 = Given_Stimuli(given_stimuli="3Q4AF", enum_type="5mixed")
# gs11.save()
# gs12 = Given_Stimuli(given_stimuli="2RHN6", enum_type="5mixed")
# gs12.save()
# gs13 = Given_Stimuli(given_stimuli="N85QR", enum_type="5mixed")
# gs13.save()
gs0 = Given_Stimuli(given_stimuli="2384", correct_order="2348", enum_type="4digit_practice")
gs0.save()
gs1 = Given_Stimuli(given_stimuli="2A3F", correct_order="23AF", enum_type="4mixed_practice")  
gs1.save()
gs2 = Given_Stimuli(given_stimuli="5736", correct_order="3567", enum_type="4digit")
gs2 = Given_Stimuli(given_stimuli="5736", correct_order="3567", enum_type="4digit")
gs2.save()
gs3 = Given_Stimuli(given_stimuli="6852", correct_order="2568", enum_type="4digit")
gs3 = Given_Stimuli(given_stimuli="6852", correct_order="2568", enum_type="4digit")
gs3.save()
gs4 = Given_Stimuli(given_stimuli="74862", correct_order="24678", enum_type="5digit")
gs4 = Given_Stimuli(given_stimuli="74862", correct_order="24678", enum_type="5digit")
gs4.save()
gs5 = Given_Stimuli(given_stimuli="35826", correct_order="23568", enum_type="5digit")
gs5 = Given_Stimuli(given_stimuli="35826", correct_order="23568", enum_type="5digit")
gs5.save()
gs6 = Given_Stimuli(given_stimuli="46715", correct_order="14567", enum_type="5digit")
gs6 = Given_Stimuli(given_stimuli="46715", correct_order="14567", enum_type="5digit")
gs6.save()
gs7 = Given_Stimuli(given_stimuli="4927", correct_order="2479", enum_type="4digit")
gs7.save()
gs8 = Given_Stimuli(given_stimuli="N54Q", correct_order="45NQ", enum_type="4mixed")
gs8 = Given_Stimuli(given_stimuli="N54Q", correct_order="45NQ", enum_type="4mixed")
gs8.save()
gs9 = Given_Stimuli(given_stimuli="H78X", correct_order="78HX", enum_type="4mixed")
gs9 = Given_Stimuli(given_stimuli="H78X", correct_order="78HX", enum_type="4mixed")
gs9.save()
gs10 = Given_Stimuli(given_stimuli="R6Y2", correct_order="26RY", enum_type="4mixed")
gs10 = Given_Stimuli(given_stimuli="R6Y2", correct_order="26RY", enum_type="4mixed")
gs10.save()
gs11 = Given_Stimuli(given_stimuli="3Q4AF", correct_order="34AFQ", enum_type="5mixed")
gs11 = Given_Stimuli(given_stimuli="3Q4AF", correct_order="34AFQ", enum_type="5mixed")
gs11.save()
gs12 = Given_Stimuli(given_stimuli="2RHN6", correct_order="26HNR", enum_type="5mixed")
gs12 = Given_Stimuli(given_stimuli="2RHN6", correct_order="26HNR", enum_type="5mixed")
gs12.save()
gs13 = Given_Stimuli(given_stimuli="N85QR", correct_order="58NQR", enum_type="5mixed")
gs13 = Given_Stimuli(given_stimuli="N85QR", correct_order="58NQR", enum_type="5mixed")
gs13.save()

#Stimulus Response creation---------------------------------------------------------------------
tests = list(Test.objects.all())
gs = list(Given_Stimuli.objects.all())

sr0 = Stimuli_Response(
    enum_type="4digit_practice", 
    response="2348",  
    response_per_click=[1, 1, 1, 1],
    test=tests[0], 
    given=gs[0]
)
sr0.save()

sr1 = Stimuli_Response(
    enum_type="4digit", 
    response="2479",  
    response_per_click=[1, 1, 1, 1],
    test=tests[0], 
    given=gs[1]
)
sr1.save()

sr2 = Stimuli_Response(
    enum_type="4digit", 
    response="3567",  
    response_per_click=[1, 1, 1, 1],
    test=tests[0], 
    given=gs[2]
)
sr2.save()

sr3 = Stimuli_Response(
    enum_type="4digit", 
    response="2568",  
    response_per_click=[1, 1, 1, 1],
    test=tests[0], 
    given=gs[3]
)
sr3.save()

sr4 = Stimuli_Response(
    enum_type="5digit", 
    response="24678",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[0], 
    given=gs[4]
)
sr4.save()

sr5 = Stimuli_Response(
    enum_type="5digit", 
    response="23568",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[0], 
    given=gs[5]
)
sr5.save()

sr6 = Stimuli_Response(
    enum_type="5digit", 
    response="14567",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[0], 
    given=gs[6]
)
sr6.save()

sr7 = Stimuli_Response(
    enum_type="4mixed_practice", 
    response="23AF",  
    response_per_click=[1, 1, 1, 1],
    test=tests[0], 
    given=gs[7]
)
sr7.save()

sr8 = Stimuli_Response(
    enum_type="4mixed", 
    response="45NQ",  
    response_per_click=[1, 1, 1, 1],
    test=tests[0], 
    given=gs[8]
)
sr8.save()

sr9 = Stimuli_Response(
    enum_type="4mixed", 
    response="78HX",  
    response_per_click=[1, 1, 1, 1],
    test=tests[0], 
    given=gs[9]
)
sr9.save()

sr10 = Stimuli_Response(
    enum_type="4mixed", 
    response="26RY",  
    response_per_click=[1, 1, 1, 1],
    test=tests[0], 
    given=gs[10]
)
sr10.save()

sr11 = Stimuli_Response(
    enum_type="5mixed", 
    response="34AFQ",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[0], 
    given=gs[11]
)
sr11.save()

sr12 = Stimuli_Response(
    enum_type="5mixed", 
    response="26HNR",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[0], 
    given=gs[12]
)
sr12.save()

sr13 = Stimuli_Response(
    enum_type="5mixed", 
    response="58NQR",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[0], 
    given=gs[13]
)
sr13.save()

sr0_1 = Stimuli_Response(
    enum_type="4digit_practice", 
    response="2348",  
    response_per_click=[1, 1, 1, 1],
    test=tests[1], 
    given=gs[0]
)
sr0_1.save()

sr1_1 = Stimuli_Response(
    enum_type="4digit", 
    response="2479",  
    response_per_click=[1, 1, 1, 1],
    test=tests[1], 
    given=gs[1]
)
sr1_1.save()

sr2_1 = Stimuli_Response(
    enum_type="4digit", 
    response="3567",  
    response_per_click=[1, 1, 1, 1],
    test=tests[1], 
    given=gs[2]
)
sr2_1.save()

sr3_1 = Stimuli_Response(
    enum_type="4digit", 
    response="2568",  
    response_per_click=[1, 1, 1, 1],
    test=tests[1], 
    given=gs[3]
)
sr3_1.save()

sr4_1 = Stimuli_Response(
    enum_type="5digit", 
    response="24678",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[1], 
    given=gs[4]
)
sr4_1.save()

sr5_1 = Stimuli_Response(
    enum_type="5digit", 
    response="23568",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[1], 
    given=gs[5]
)
sr5_1.save()

sr6_1 = Stimuli_Response(
    enum_type="5digit", 
    response="14567",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[1], 
    given=gs[6]
)
sr6_1.save()

sr7_1 = Stimuli_Response(
    enum_type="4mixed_practice", 
    response="23AF",  
    response_per_click=[1, 1, 1, 1],
    test=tests[1], 
    given=gs[7]
)
sr7_1.save()

sr8_1 = Stimuli_Response(
    enum_type="4mixed", 
    response="45NQ",  
    response_per_click=[1, 1, 1, 1],
    test=tests[1], 
    given=gs[8]
)
sr8_1.save()

sr9_1 = Stimuli_Response(
    enum_type="4mixed", 
    response="78HX",  
    response_per_click=[1, 1, 1, 1],
    test=tests[1], 
    given=gs[9]
)
sr9_1.save()

sr10_1 = Stimuli_Response(
    enum_type="4mixed", 
    response="26RY",  
    response_per_click=[1, 1, 1, 1],
    test=tests[1], 
    given=gs[10]
)
sr10_1.save()

sr11_1 = Stimuli_Response(
    enum_type="5mixed", 
    response="34AFQ",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[1], 
    given=gs[11]
)
sr11_1.save()

sr12_1 = Stimuli_Response(
    enum_type="5mixed", 
    response="26HNR",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[1], 
    given=gs[12]
)
sr12_1.save()

sr13_1 = Stimuli_Response(
    enum_type="5mixed", 
    response="58NQR",  
    response_per_click=[1, 1, 1, 1, 1],
    test=tests[1], 
    given=gs[13]
)
sr13_1.save()

sr0_2 = Stimuli_Response(
    enum_type="4digit_practice", 
    response="2348",  
    response_per_click=[2, 2, 2, 2],
    test=tests[2], 
    given=gs[0]
)
sr0_2.save()

sr1_2 = Stimuli_Response(
    enum_type="4digit", 
    response="2479",  
    response_per_click=[2, 2, 2, 2],
    test=tests[2], 
    given=gs[1]
)
sr1_2.save()

sr2_2 = Stimuli_Response(
    enum_type="4digit", 
    response="3567",  
    response_per_click=[2, 2, 2, 2],
    test=tests[2], 
    given=gs[2]
)
sr2_2.save()

sr3_2 = Stimuli_Response(
    enum_type="4digit", 
    response="2568",  
    response_per_click=[2, 2, 2, 2],
    test=tests[2], 
    given=gs[3]
)
sr3_2.save()

sr4_2 = Stimuli_Response(
    enum_type="5digit", 
    response="24678",  
    response_per_click=[2, 2, 2, 2, 2],
    test=tests[2], 
    given=gs[4]
)
sr4_2.save()

sr5_2 = Stimuli_Response(
    enum_type="5digit", 
    response="23568",  
    response_per_click=[2, 2, 2, 2, 2],
    test=tests[2], 
    given=gs[5]
)
sr5_2.save()

sr6_2 = Stimuli_Response(
    enum_type="5digit", 
    response="14567",  
    response_per_click=[2, 2, 2, 2, 2],
    test=tests[2], 
    given=gs[6]
)
sr6_2.save()

sr7_2 = Stimuli_Response(
    enum_type="4mixed_practice", 
    response="23AF",  
    response_per_click=[2, 2, 2, 2],
    test=tests[2], 
    given=gs[7]
)
sr7_2.save()

sr8_2 = Stimuli_Response(
    enum_type="4mixed", 
    response="45NQ",  
    response_per_click=[2, 2, 2, 2],
    test=tests[2], 
    given=gs[8]
)
sr8_2.save()

sr9_2 = Stimuli_Response(
    enum_type="4mixed", 
    response="78HX",  
    response_per_click=[2, 2, 2, 2],
    test=tests[2], 
    given=gs[9]
)
sr9_2.save()

sr10_2 = Stimuli_Response(
    enum_type="4mixed", 
    response="26RY",  
    response_per_click=[2, 2, 2, 2],
    test=tests[2], 
    given=gs[10]
)
sr10_2.save()

sr11_2 = Stimuli_Response(
    enum_type="5mixed", 
    response="34AFQ",  
    response_per_click=[2, 2, 2, 2, 2],
    test=tests[2], 
    given=gs[11]
)
sr11_2.save()

sr12_2 = Stimuli_Response(
    enum_type="5mixed", 
    response="26HNR",  
    response_per_click=[2, 2, 2, 2, 2],
    test=tests[2], 
    given=gs[12]
)
sr12_2.save()

sr13_2 = Stimuli_Response(
    enum_type="5mixed", 
    response="58NQR",  
    response_per_click=[2, 2, 2, 2, 2],
    test=tests[2], 
    given=gs[13]
)
sr13_2.save()

sr0_3 = Stimuli_Response(
    enum_type="4digit_practice", 
    response="2348",  
    response_per_click=[2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[0]
)
sr0_3.save()

sr1_3 = Stimuli_Response(
    enum_type="4digit", 
    response="2479",  
    response_per_click=[2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[1]
)
sr1_3.save()

sr2_3 = Stimuli_Response(
    enum_type="4digit", 
    response="3567",  
    response_per_click=[2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[2]
)
sr2_3.save()

sr3_3 = Stimuli_Response(
    enum_type="4digit", 
    response="2568",  
    response_per_click=[2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[3]
)
sr3_3.save()

sr4_3 = Stimuli_Response(
    enum_type="5digit", 
    response="24678",  
    response_per_click=[2.5, 2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[4]
)
sr4_3.save()

sr5_3 = Stimuli_Response(
    enum_type="5digit", 
    response="23568",  
    response_per_click=[2.5, 2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[5]
)
sr5_3.save()

sr6_3 = Stimuli_Response(
    enum_type="5digit", 
    response="14567",  
    response_per_click=[2.5, 2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[6]
)
sr6_3.save()

sr7_3 = Stimuli_Response(
    enum_type="4mixed_practice", 
    response="23AF",  
    response_per_click=[2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[7]
)
sr7_3.save()

sr8_3 = Stimuli_Response(
    enum_type="4mixed", 
    response="45NQ",  
    response_per_click=[2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[8]
)
sr8_3.save()

sr9_3 = Stimuli_Response(
    enum_type="4mixed", 
    response="78HX",  
    response_per_click=[2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[9]
)
sr9_3.save()

sr10_3 = Stimuli_Response(
    enum_type="4mixed", 
    response="26RY",  
    response_per_click=[2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[10]
)
sr10_3.save()

sr11_3 = Stimuli_Response(
    enum_type="5mixed", 
    response="34AFQ",  
    response_per_click=[2.5, 2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[11]
)
sr11_3.save()

sr12_3 = Stimuli_Response(
    enum_type="5mixed", 
    response="26HNR",  
    response_per_click=[2.5, 2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[12]
)
sr12_3.save()

sr13_3 = Stimuli_Response(
    enum_type="5mixed", 
    response="58NQR",  
    response_per_click=[2.5, 2.5, 2.5, 2.5, 2.5],
    test=tests[3], 
    given=gs[13]
)
sr13_3.save()

sr0_4 = Stimuli_Response(
    enum_type="4digit_practice", 
    response="2348",  
    response_per_click=[3, 3, 3, 3],
    test=tests[4], 
    given=gs[0]
)
sr0_4.save()

sr1_4 = Stimuli_Response(
    enum_type="4digit", 
    response="2479",  
    response_per_click=[3, 3, 3, 3],
    test=tests[4], 
    given=gs[1]
)
sr1_4.save()

sr2_4 = Stimuli_Response(
    enum_type="4digit", 
    response="3567",  
    response_per_click=[3, 3, 3, 3],
    test=tests[4], 
    given=gs[2]
)
sr2_4.save()

sr3_4 = Stimuli_Response(
    enum_type="4digit", 
    response="2568",  
    response_per_click=[3, 3, 3, 3],
    test=tests[4], 
    given=gs[3]
)
sr3_4.save()

sr4_4 = Stimuli_Response(
    enum_type="5digit", 
    response="24678",  
    response_per_click=[3, 3, 3, 3, 3],
    test=tests[4], 
    given=gs[4]
)
sr4_4.save()

sr5_4 = Stimuli_Response(
    enum_type="5digit", 
    response="23568",  
    response_per_click=[3, 3, 3, 3, 3],
    test=tests[4], 
    given=gs[5]
)
sr5_4.save()

sr6_4 = Stimuli_Response(
    enum_type="5digit", 
    response="14567",  
    response_per_click=[3, 3, 3, 3, 3],
    test=tests[4], 
    given=gs[6]
)
sr6_4.save()

sr7_4 = Stimuli_Response(
    enum_type="4mixed_practice", 
    response="23AF",  
    response_per_click=[3, 3, 3, 3],
    test=tests[4], 
    given=gs[7]
)
sr7_4.save()

sr8_4 = Stimuli_Response(
    enum_type="4mixed", 
    response="45NQ",  
    response_per_click=[3, 3, 3, 3],
    test=tests[4], 
    given=gs[8]
)
sr8_4.save()

sr9_4 = Stimuli_Response(
    enum_type="4mixed", 
    response="78HX",  
    response_per_click=[3, 3, 3, 3],
    test=tests[4], 
    given=gs[9]
)
sr9_4.save()

sr10_4 = Stimuli_Response(
    enum_type="4mixed", 
    response="26RY",  
    response_per_click=[3, 3, 3, 3],
    test=tests[4], 
    given=gs[10]
)
sr10_4.save()

sr11_4 = Stimuli_Response(
    enum_type="5mixed", 
    response="34AFQ",  
    response_per_click=[3, 3, 3, 3, 3],
    test=tests[4], 
    given=gs[11]
)
sr11_4.save()

sr12_4 = Stimuli_Response(
    enum_type="5mixed", 
    response="26HNR",  
    response_per_click=[3, 3, 3, 3, 3],
    test=tests[4], 
    given=gs[12]
)
sr12_4.save()

sr13_4 = Stimuli_Response(
    enum_type="5mixed", 
    response="58NQR",  
    response_per_click=[3, 3, 3, 3, 3],
    test=tests[4], 
    given=gs[13]
)
sr13_4.save()

n0 = Notification(status=0,message='Patient has completed their test!')
n0.save()
n0.users.add(doctors[0])
n1 = Notification(status=1,message='Patient has completed their test!')
n1.save()
n1.users.add(doctors[0])
n2 = Notification(status=0,message='Patient has completed their test!')
n2.save()
n2.users.add(doctors[1])
n3 = Notification(status=0,message='Patient has completed their test!')
n3.save()
n3.users.add(doctors[2])
n4 = Notification(status=0,message='Patient has completed their test!')
n4.save()
n4.users.add(doctors[3])