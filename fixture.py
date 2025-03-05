from django.db import models
from PPST.models import Doctor, Test, Given_Stimuli, Stimuli_Response, Notification

for c in [Doctor, Test, Given_Stimuli, Stimuli_Response, Notification]:
    c.objects.all().delete()

import random
import string
import datetime
from django.utils.timezone import now
#---------------------------------------------------------------------------
# Sample first and last names for randomization
first_names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]
last_names = ["Smith", "Jones", "Taylor", "Brown", "Miller"]

# Create 5 doctor users
for i in range(5):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    username = f"doctor{i}"
    email = f"{first_name.lower()}.{last_name.lower()}@hospital.com"
    password = "SecurePass123"  # Ideally, use a randomly generated password

    # Create doctor user
    doctor = Doctor.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    doctor.save()
    print(f"Created Doctor {username} ({first_name} {last_name})")
#---------------------------------------------------------------------------
# Fetch all doctors (we will assign one at random per test)
doctors = list(Doctor.objects.all())

# Ensure we have at least one doctor available
if not doctors:
    raise ValueError("No doctors found in the database! Please add some first.")

# Create 3 Test instances
for i in range(10):
    test_id = f"t{i}"  # Naming test instances as t0, t1, ..., t9
    time_started = now()
    time_ended = time_started + datetime.timedelta(minutes=random.randint(5, 60))  # 5 to 60 min duration
    patient_age = random.randint(40, 110)
    doctor = random.choice(doctors)  # Assign a random doctor

    test = Test(
        test_id=test_id,
        time_started=time_started,
        time_ended=time_ended,
        status=0,  # Default status
        patient_age=patient_age,
        doctor=doctor
    )

    test.save()
    print(f"Created Test {test.test_id} (Age: {patient_age}, Doctor: {doctor.id})")
#-------------------------------------------------------------------------------------------
# Stimuli for test t0
gs0 = Given_Stimuli(given_id=0,given_stimuli="5432", enum_type="4digit_practice")
gs0.save()
gs1 = Given_Stimuli(given_id=1,given_stimuli="6543", enum_type="4digit")
gs1.save()
gs2 = Given_Stimuli(given_id=2,given_stimuli="7654", enum_type="4digit")
gs2.save()
gs3 = Given_Stimuli(given_id=3,given_stimuli="8765", enum_type="4digit")
gs3.save()
gs4 = Given_Stimuli(given_id=4,given_stimuli="65432", enum_type="5digit")
gs4.save()
gs5 = Given_Stimuli(given_id=5,given_stimuli="76543", enum_type="5digit")
gs5.save()
gs6 = Given_Stimuli(given_id=6,given_stimuli="87654", enum_type="5digit")
gs6.save()
gs7 = Given_Stimuli(given_id=7,given_stimuli="32ba", enum_type="4mixed_practice")
gs7.save()
gs8 = Given_Stimuli(given_id=8,given_stimuli="43cb", enum_type="4mixed")
gs8.save()
gs9 = Given_Stimuli(given_id=9,given_stimuli="54dc", enum_type="4mixed")
gs9.save()
gs10 = Given_Stimuli(given_id=10,given_stimuli="65ed", enum_type="4mixed")
gs10.save()
gs11 = Given_Stimuli(given_id=11,given_stimuli="765fe", enum_type="5mixed")
gs11.save()
gs12 = Given_Stimuli(given_id=12,given_stimuli="8765gf", enum_type="5mixed")
gs12.save()
gs13 = Given_Stimuli(given_id=13,given_stimuli="2dcba", enum_type="5mixed")
gs13.save()

# Define the sequence of enum types
enum_types_sequence = [
    "4digit_practice", "4digit", "4digit", "4digit",
    "5digit", "5digit", "5digit",
    "4mixed_practice", "4mixed", "4mixed", "4mixed",
    "5mixed", "5mixed", "5mixed"
]

# Function to generate responses based on enum type
def generate_response(enum_type):
    if "digit" in enum_type:
        length = 4 if "4digit" in enum_type else 5
        return "".join(random.choices(string.digits, k=length))
    elif "mixed" in enum_type:
        length = 4 if "4mixed" in enum_type else 5
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Fetch or create tests (assuming there are exactly 10 test objects t0 to t9)
tests = list(Test.objects.all()[:10])  # Ensure we get exactly 10 test instances

# Iterate over each test and assign the stimuli responses
for test in tests:
    x = 0
    for enum_type in enum_types_sequence:
        response = generate_response(enum_type)
        response_per_click = random.randint(1, 5)
        gs = Given_Stimuli.objects.all()[x]
        sr = Stimuli_Response(
            enum_type=enum_type,
            response=response,
            response_per_click=response_per_click,
            test=test,
            given = gs
        )
        sr.save()
        print(f"Created {sr} for test {test.test_id}")
        x = x + 1