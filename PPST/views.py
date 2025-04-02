import tempfile
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from PPST.models import Doctor, Test, Stimuli_Response, Given_Stimuli, Notification
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import logging
import json
import csv
import tempfile
import json

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


import random
from django.shortcuts import render

def next_page(request, selected_values):
    if request.method == "POST":
        selected_values = request.POST.get('selected_values', '')
        return render(request, 'next_page.html', {'selected_values': selected_values})
    return render(request, 'next_page.html')

from django.http import HttpResponseNotFound

def testScreen(request, testId):
    # Check if the testId exists in the database
    test_exists = Test.objects.filter(test_id=testId).exists()
    
    if not test_exists:
        return HttpResponseNotFound("Test ID not found. Please contact your doctor.")  # Return a 404 response if test_id is invalid

    # Fetch the valid test object
    test_instance = Test.objects.get(test_id=testId)

    # Retrieve all stimuli objects
    stimuli_objects = Given_Stimuli.objects.all()
    stimuli_list = [stimulus.given_stimuli for stimulus in stimuli_objects]
    stimuli_enum = [stimulus.enum_type for stimulus in stimuli_objects]

    return render(request, 'testScreen.html', {
        'stimuli_list': stimuli_list,
        'test_id': test_instance,
        'stimuli_objects': stimuli_objects,
        'stimuli_enum': stimuli_enum
    })
def test(request):
    return HttpResponse("Hello World!")


def doctorHomePage(request, username):

    doctors = Doctor.objects.first()

    selected_doctor_id = request.GET.get('doctor')

    try:
        # Fetch the doctor by username
        selected_doctor = Doctor.objects.get(username=username)
        # Fetch notifications for the selected doctor
        notifications = Notification.objects.filter(users=selected_doctor)
    except Doctor.DoesNotExist:
        # If the doctor does not exist, raise a 404 error
        raise Http404("Doctor not found")

    return render(request, 'doctorHomePage.html', {
        'doctors': doctors,
        'notifications': notifications,
        'selected_doctor_id': selected_doctor_id,
        'doctor_first_name': selected_doctor.first_name,
        'doctor_last_name': selected_doctor.last_name
    })
  
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
            return redirect('PPST:doctorHomePage')
        else:
            # Invalid login
            messages.error(request, 'Invalid username or password')
    else:
        return render(request, 'doctorLoginInitial.html')

def testInfo(request):
    QUESTIONS_PER_TEST = 14
    percentages = []
    notEmpty = False

    currDoc = get_user(request)
    #currDoc = Doctor.objects.get(username = "doctor0") # use for debugging
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

def doctorHomePage(request):
    return render(request, 'doctorHomePage.html')

def average_statistics(request):
    # Fetch all test data
    tests = Test.objects.values_list('patient_age', flat=True)

    if not tests:
        age_data = { "0-9": 0, "10-19": 0, "20-29": 0, "30-39": 0, "40-49": 0,
                     "50-59": 0, "60-69": 0, "70-79": 0, "80-89": 0, "90+": 0 }
        accuracy_data = {key: 0 for key in age_data.keys()}  # Initialize accuracy as 0
    else:
        # Convert to DataFrame
        df = pd.DataFrame({'patient_age': tests})

        # Define age bins and labels
        bins = [0, 9, 19, 29, 39, 49, 59, 69, 79, 89, float('inf')]
        labels = ["0-9", "10-19", "20-29", "30-39", "40-49", 
                  "50-59", "60-69", "70-79", "80-89", "90+"]

        # Categorize ages into bins
        df['age_group'] = pd.cut(df['patient_age'], bins=bins, labels=labels, right=True)

        # Count occurrences in each group
        age_data = df['age_group'].value_counts().sort_index().to_dict()

        # Initialize accuracy tracking
        accuracy_data = {key: [] for key in labels}  

        # Fetch all responses and match them to the correct answers
        responses = Stimuli_Response.objects.select_related('given')

        for response in responses:
            correct = response.given.correct_order.strip()
            user_response = response.response.strip()

            if len(correct) == len(user_response) and len(correct) > 0:
                # Calculate exact character match percentage
                match_count = sum(1 for c1, c2 in zip(correct, user_response) if c1 == c2)
                accuracy_percentage = (match_count / len(correct)) * 100
            else:
                accuracy_percentage = 0  # If lengths don't match, assume 0% accuracy

            # Get the corresponding test age and categorize it
            age = response.test.patient_age
            age_group = pd.cut([age], bins=bins, labels=labels, right=True)[0]

            if age_group in accuracy_data:
                accuracy_data[age_group].append(accuracy_percentage)

        # Compute average accuracy for each age group
        for key in accuracy_data.keys():
            if accuracy_data[key]:  # Avoid division by zero
                accuracy_data[key] = sum(accuracy_data[key]) / len(accuracy_data[key])
            else:
                accuracy_data[key] = 0  # If no data, default to 0%

    # Convert data to JSON for the frontend
    return render(request, 'average_statistics.html', {
        'labels': json.dumps(list(age_data.keys())),
        'values': json.dumps(list(age_data.values())),
        'accuracy_labels': json.dumps(list(accuracy_data.keys())),
        'accuracy_values': json.dumps(list(accuracy_data.values()))
    })