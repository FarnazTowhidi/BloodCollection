from django.forms import ModelForm
from .models import Patient, Patient_BloodSample

class PatientForm(ModelForm):
  class Meta:
    model = Patient
    fields = ['name', 'age', 'sex', 'family_doctor','HealthCare_number']

class PatientBloodSampleForm(ModelForm):
    class Meta:
        model = Patient_BloodSample
        fields = ['collection_date', 'ordering_Physician']