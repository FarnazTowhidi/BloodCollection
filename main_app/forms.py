from django.forms import ModelForm
from .models import Patient, BloodSamples

class PatientForm(ModelForm):
  class Meta:
    model = Patient
    fields = ['name', 'age', 'sex', 'familyDoctor','HealthCareNumber']

class PatientBloodSampleForm(ModelForm):
    class Meta:
        model = BloodSamples
        fields = ['collectionDate', 'orderingPhysician']