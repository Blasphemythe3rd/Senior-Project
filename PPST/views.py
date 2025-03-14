import tempfile
from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, Test, Stimuli_Response
import csv
from django.http import FileResponse

# Create your views here.

def test(request):
    return HttpResponse("Hello World!")

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
            "Accuracy": _calculate_accuracies(test),
            "Average Response Time": avg_response
        }
    
    # stores CSV as temporary file on local machine, not in project (debugged w/ chatgpt)
    with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as csvfile:
        writer = csv.writer(csvfile)
        # create top table
        writer.writerow(["Test ID", "Time Start", "Time End", "Status", "Age", "Accuracy", "Average Response Time"])
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