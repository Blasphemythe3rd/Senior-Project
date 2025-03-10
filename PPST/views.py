import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Test, Stimuli_Response, Given_Stimuli

# Create your views here.

def test(request):
    return HttpResponse("Hello World!")

def doctor(request):
    return render(request, "DoctorsNavigations/notifications.html", {})

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
    return render(request, 'DoctorsNavigations/average_statistics.html', {
        'labels': json.dumps(list(age_data.keys())),
        'values': json.dumps(list(age_data.values())),
        'accuracy_labels': json.dumps(list(accuracy_data.keys())),
        'accuracy_values': json.dumps(list(accuracy_data.values()))
    })