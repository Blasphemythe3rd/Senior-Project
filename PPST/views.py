import random
from django.shortcuts import render
from .models import Given_Stimuli

def practiceTest(request):
    return render(request,'practiceTest.html')

def testScreen(request):
    stimuli_objects = Given_Stimuli.objects.all()
    stimuli_list = [stimulus.given_stimuli for stimulus in stimuli_objects]

    return render(request, 'testScreen.html', {'stimuli_list': stimuli_list})