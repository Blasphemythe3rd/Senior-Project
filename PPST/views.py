from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from PPST.models import Doctor, Test, Stimuli_Response
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def test(request):
    return HttpResponse("Hello World!")

@csrf_exempt
def admin_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            logger.info(f"Attempting to authenticate user: {username}")

            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_staff:  
                login(request, user)  
                logger.info(f"User {username} authenticated successfully")
                return JsonResponse({'success': True})
            else:
                logger.warning(f"Authentication failed for user: {username}")
                return JsonResponse({'success': False, 'error': 'Invalid credentials or not an admin.'})
        except Exception as e:
            logger.error(f"Error during login: {e}")
            return JsonResponse({'success': False, 'error': 'An error occurred. Please try again.'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def admin_page(request):
    doctors = Doctor.objects.all()  
    return render(request, "admin.html", {"doctors": doctors})

@require_GET
def list_doctors(request):
    doctors = Doctor.objects.all().values("id", "first_name", "last_name", "email", "username")
    return JsonResponse(list(doctors), safe=False)

@require_GET
def fetch_test_details(request, test_id):
    try:
        test = Test.objects.get(test_id=test_id)
        stimuli_responses = Stimuli_Response.objects.filter(test=test).values("enum_type", "response", "response_per_click", "given__given_stimuli", "given__correct_order")
        return JsonResponse({
            "test_id": test.test_id,
            "time_started": test.time_started,
            "time_ended": test.time_ended,
            "status": test.status,
            "patient_age": test.patient_age,
            "stimuli_responses": list(stimuli_responses)
        })
    except Test.DoesNotExist:
        return JsonResponse({"error": "Test not found"}, status=404)

@require_GET
def doctor_tests(request, doctor_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        tests = Test.objects.filter(doctor=doctor)
        
        test_details = []
        for test in tests:
            stimuli_responses = Stimuli_Response.objects.filter(test=test).values("enum_type", "response", "response_per_click", "given__given_stimuli", "given__correct_order")
            
            test_details.append({
                "test_id": test.test_id,
                "time_started": test.time_started,
                "time_ended": test.time_ended,
                "status": test.status,
                "patient_age": test.patient_age,
                "stimuli_responses": list(stimuli_responses)
            })
        
        return JsonResponse({
            "doctor": f"{doctor.first_name} {doctor.last_name}",
            "tests": test_details
        })
    except Doctor.DoesNotExist:
        return JsonResponse({"error": "Doctor not found"}, status=404)
    
@csrf_exempt
@require_POST
def add_doctor(request):
    """Adds a new doctor, ensuring a unique username in 'doctor#' format."""
    try:
        data = json.loads(request.body)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")

        if not (first_name and last_name and email):
            return JsonResponse({"error": "Missing fields"}, status=400)

        doctor_count = 0
        while True:
            username = f"doctor{doctor_count}"
            if not Doctor.objects.filter(username=username).exists():
                break
            doctor_count += 1

        new_doctor = Doctor.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
        new_doctor.set_password("defaultpassword123")  
        new_doctor.save()

        return JsonResponse({
            "message": "Doctor added successfully!",
            "doctor_id": new_doctor.id,
            "username": username
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)