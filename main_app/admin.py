from django.contrib import admin
from .models import Patient, BloodSamples, Medications, BloodSampleResult
# Register your models here.

admin.site.register(Patient)
admin.site.register(BloodSamples)
admin.site.register(BloodSampleResult)
admin.site.register(Medications)