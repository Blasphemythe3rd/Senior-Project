from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, Notification

# Create your views here.

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