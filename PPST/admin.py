from django.contrib import admin

from .models import Given_Stimuli, Stimuli_Response, Test, Doctor, Notification

# Register your models here.
admin.site.register(Given_Stimuli)
admin.site.register(Stimuli_Response)
admin.site.register(Test)
admin.site.register(Doctor)
admin.site.register(Notification)
