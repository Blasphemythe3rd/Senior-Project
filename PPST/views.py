from django.shortcuts import render
from .models import Given_Stimuli
import random

# View to render the test page with random stimuli
def test_page(request):
    # Fetch all stimuli from the database
    stimuli_list = list(Given_Stimuli.objects.all())
    
    # Choose a random stimulus
    stimulus = random.choice(stimuli_list) if stimuli_list else None
    
    # Pass the stimulus to the template
    context = {
        'stimulus': stimulus
    }
    
    return render(request, 'PPST/test_page.html', context)
