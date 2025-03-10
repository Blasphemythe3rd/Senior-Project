import random
from django.shortcuts import render
from .models import Given_Stimuli

def practiceTest(request):
    return render(request,'practiceTest.html')

def testScreen(request):
    stimuli_0 = Given_Stimuli.objects.first()  # Get the first object (you can change this query)
    
    # If no object exists, provide an empty string or handle it differently
    given_stimuli_str = stimuli_0.given_stimuli if stimuli_0 else ""

    return render(request, 'testScreen.html', {'given_stimuli_str': given_stimuli_str})
