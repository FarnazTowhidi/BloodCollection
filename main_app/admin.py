from django.contrib import admin
from .models import Patient, BloodSamples, Medications, BloodSampleResult, Photo
# Register your models here.


class MyAdminSite(admin.AdminSite):
    site_header = 'Monty Python administration'
    site_title = 'farnaz'

admin.site.register(Patient)
admin.site.register(BloodSamples)
admin.site.register(BloodSampleResult)
admin.site.register(Medications)
admin.site.register(Photo)