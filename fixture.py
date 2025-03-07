from django.db import models
from PPST.models import Doctor, Test, Given_Stimuli, Stimuli_Response, Notification

# Delete all existing objects
for model in [Doctor, Test, Given_Stimuli, Stimuli_Response, Notification]:
    model.objects.all().delete()

import random
import string
import datetime
from django.utils.timezone import now

# ----------------- Doctor Creation -----------------
doctors_data = [
    {"first_name": "Alice", "last_name": "Smith"},
    {"first_name": "Bob", "last_name": "Jones"},
    {"first_name": "Charlie", "last_name": "Brown"},
    {"first_name": "Diana", "last_name": "Taylor"},
    {"first_name": "Edward", "last_name": "Miller"},
    {"first_name": "Fiona", "last_name": "Clark"},
]

doctors = []
for i, doctor_info in enumerate(doctors_data):
    username = f"doctor{i}"
    email = f"{doctor_info['first_name'].lower()}.{doctor_info['last_name'].lower()}@hospital.com"

    doctor = Doctor.objects.create_user(
        username=username,
        email=email,
        password="SecurePass123",
        first_name=doctor_info["first_name"],
        last_name=doctor_info["last_name"],
    )
    doctors.append(doctor)

print(f"Total Doctors Created: {len(doctors)}")

# ----------------- Test Creation -----------------
tests = []
for i in range(10):
    test = Test(
        test_id=f"t{i}",
        time_started=now(),
        time_ended=now() + datetime.timedelta(minutes=random.randint(5, 60)),
        status=0,
        patient_age=random.randint(40, 110),
        doctor=random.choice(doctors),
    )
    tests.append(test)

Test.objects.bulk_create(tests)
tests = list(Test.objects.all())  # Fetch the tests after bulk creation

print(f"Total Tests Created: {len(tests)}")

# ----------------- Given Stimuli Creation -----------------
stimuli_data = [
    ("5432", "4digit_practice"), ("6543", "4digit"), ("7654", "4digit"), ("8765", "4digit"),
    ("65432", "5digit"), ("76543", "5digit"), ("87654", "5digit"),
    ("32ba", "4mixed_practice"), ("43cb", "4mixed"), ("54dc", "4mixed"), ("65ed", "4mixed"),
    ("765fe", "5mixed"), ("875gf", "5mixed"), ("23cba", "5mixed")
]

given_stimuli_objects = [Given_Stimuli(given_stimuli=s[0], enum_type=s[1]) for s in stimuli_data]
Given_Stimuli.objects.bulk_create(given_stimuli_objects)
given_stimuli = list(Given_Stimuli.objects.order_by("id"))

print(f"Total Given Stimuli Created: {len(given_stimuli)}")

# ----------------- Stimuli Response Creation -----------------

def generate_response(enum_type):
    """Generate appropriate response format based on type."""
    if "digit" in enum_type:
        return "".join(random.choices(string.digits, k=4 if "4digit" in enum_type else 5))
    elif "mixed" in enum_type:
        num_count = 2 if "4mixed" in enum_type else 2  # Always 2 numbers
        letter_count = 2 if "4mixed" in enum_type else 3  # 2 letters for 4mixed, 3 for 5mixed
        numbers = random.choices(string.digits, k=num_count)
        letters = random.choices(string.ascii_uppercase, k=letter_count)
        return "".join(random.sample(numbers + letters, len(numbers) + len(letters)))  # Shuffle

# Create Stimuli Responses
stimuli_responses = []
for test in tests:
    for idx, enum_type in enumerate(stimuli_data):
        stimuli_responses.append(
            Stimuli_Response(
                enum_type=enum_type[1],
                response=generate_response(enum_type[1]),
                response_per_click=random.randint(1, 5),
                test=test,
                given=given_stimuli[idx],
            )
        )

Stimuli_Response.objects.bulk_create(stimuli_responses)

print(f"Total Stimuli Responses Created: {len(stimuli_responses)}")
