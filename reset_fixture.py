from django.contrib.auth.models import User
from PPST.models import Test, Doctor, Notification, Stimuli_Response

# Delete all existing data
print("Deleting all fixture data...")

Stimuli_Response.objects.all().delete()
Test.objects.all().delete()
Notification.objects.all().delete()
Doctor.objects.all().delete()


print("All fixture data deleted successfully!")
