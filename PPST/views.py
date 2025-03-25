import random
from django.shortcuts import render
from .models import Given_Stimuli

def practiceTest(request):
    return render(request,'practiceTest.html')

def testScreen(request):
    stimuli_objects = Given_Stimuli.objects.all()
    stimuli_list = [stimulus.given_stimuli for stimulus in stimuli_objects]

    return render(request, 'testScreen.html', {'stimuli_list': stimuli_list})
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from PPST.models import Doctor, Test, Stimuli_Response
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
import csv

# Create your views here.

import random
from django.shortcuts import render
from .models import Given_Stimuli

def practiceTest(request):
    return render(request,'practiceTest.html')

def testScreen(request):
    stimuli_objects = Given_Stimuli.objects.all()
    stimuli_list = [stimulus.given_stimuli for stimulus in stimuli_objects]

    return render(request, 'testScreen.html', {'stimuli_list': stimuli_list})

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

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('PPST:doctor_login')
        else:
            # Invalid login
            return render(request, 'doctorLoginInitial.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'doctorLoginInitial.html')

def testInfo(request):
    QUESTIONS_PER_TEST = 14
    percentages = []
    notEmpty = False

    currDoc = Doctor.objects.get(username = "doctor0") # will get the doctor that is signed in (waiting for sign in function)
    tests = Test.objects.filter(doctor = currDoc)

    for test in tests: # calculate correct response %
        percentages.append(_calculate_accuracies(test))

    zippedTests = zip(tests, percentages) # can use both in django for each:  {% for test, percentage in tests %}

    if(tests): # allows webpage to display no tests screen rather than empty table
        notEmpty = True

    return render(request, "testInfo.html", {
        'doctor' : currDoc,
        'notEmpty' : notEmpty,
        'tests' : zippedTests
    })

def download_test(request, test_id):
    spreadsheet = []

    # https://www.geeksforgeeks.org/writing-csv-files-in-python/ 
    test = Test.objects.get(test_id = test_id)
    responses = Stimuli_Response.objects.filter(test = test)
    response_times = []
    stimulus_num = 1
    for response in responses:
        response_times.extend(response.response_per_click)
        dict = { # per stimulus part
            "Stimulus #": stimulus_num,
            "Response Time Per Click": response.response_per_click,
            "Responses": response.response,
            "Total Stimuli Time" : sum(response.response_per_click)
        }
        stimulus_num += 1

        spreadsheet.append(dict)

    avg_response = sum(response_times)/len(response_times)
    test_info = { # overall test info
            "Test ID": test.test_id,
            "Time Start": test.time_started,
            "Time End": test.time_ended,
            "Status": test.status,
            "Age": test.patient_age, 
            "Accuracy %": _calculate_accuracies(test),
            "Average Response Time": avg_response
        }
    
    # stores CSV as temporary file on local machine, not in project (debugged w/ chatgpt)
    with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as csvfile:
        writer = csv.writer(csvfile)
        # create top table
        writer.writerow(["Test ID", "Time Start", "Time End", "Status", "Age", "Accuracy %", "Average Response Time"])
        writer.writerow([
            test_info["Test ID"],
            test_info["Time Start"],
            test_info["Time End"],
            test_info["Status"],
            test_info["Age"],
            test_info["Accuracy %"],
            test_info["Average Response Time"]
        ])

        writer.writerow([])
        # add bottom table
        writer.writerow(["Stimulus #", "Response Time Per Click", "Responses", "Total Stimuli Time"])
        for row in spreadsheet: # add to csv row by row
            writer.writerow([
                row["Stimulus #"],
                row["Response Time Per Click"],
                row["Responses"],
                row["Total Stimuli Time"]
            ])

    
    tmpfile_path = csvfile.name

    response = FileResponse(open(tmpfile_path, 'rb'), as_attachment=True, filename="test_data.csv")

    return response

def _calculate_accuracies(test):
    QUESTIONS_PER_TEST = 14

    responses = Stimuli_Response.objects.filter(test = test)
    correct = 0
    for response in responses:
        if(response.response == response.given.correct_order):
            correct+=1

    return round(correct/QUESTIONS_PER_TEST * 100, 2)