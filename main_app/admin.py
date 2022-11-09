from django.contrib import admin
from .models import Patient, Patient_BloodSample, BloodSample_Result
# Register your models here.

admin.site.register(Patient)
admin.site.register(Patient_BloodSample)
admin.site.register(BloodSample_Result)