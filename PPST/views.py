from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from PPST.models import Doctor, Test
from django.core.mail import send_mail
from django.conf import settings
import json


# Create your views here.

def test(request):
    return HttpResponse("Hello World!")

@require_POST
def createTest(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body) #parse the json data from the request
            recipient_email = data.get("email")
            patient_age = data.get("age")

            if not recipient_email: #check for email
                return JsonResponse({"error": "No email provided"}, status=400)

            doctor = Doctor.objects.first() #get the first doctor (hardcoded for now will change when I can)
            if not doctor:
                return JsonResponse({"error": "No doctor available in the system"}, status=500)

            new_test = Test.objects.create(patient_age=patient_age, doctor=doctor) #create a new test object
            
            subject = "Test Link for PPST"
            message = f"A new test has been created for you with ID: http://127.0.0.1:8000/PPST/{new_test.test_id}" #message to be sent to the user with link(link will need to be changed)
            
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])

            return JsonResponse({"message": "Email sent successfully!",
                                 "test_id": new_test.test_id,
                                 "doctor": doctor.last_name,
                                })  
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)  


@require_GET
def ppstCreate(request): #this shows the site
    return render(request, "createTest.html", {})

def generateTest(request): #this does nothing right now its just so link kinda works but not yet i need other peoples implementations
    return render(request, "generateTest.html", {})

