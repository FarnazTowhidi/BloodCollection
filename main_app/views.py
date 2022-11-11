from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Patient
from .models import BloodSamples
from .models import Medications
from .models import BloodSampleResult 
from .forms import PatientBloodSampleForm

class patient_create(CreateView):
  model = Patient
  fields = ['name', 'age', 'sex', 'age', 'HealthCareNumber', 'familyDoctor']


class patient_update(UpdateView):
    model = Patient
    fields = '__all__'
    patients = Patient.objects.all()
    success_url = "/patients"


class patients_delete(DeleteView):
    model = Patient
    success_url = '/patients/'


def home(request):
  return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def patients_index(request):   
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', {'patients':patients})
    

def patients_details(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    medication_patient_doesnt_have = Medications.objects.exclude(id__in = patient.medications.all().values_list('id'))
    patientBloodSample_form = PatientBloodSampleForm()
    return render(request, 'patients/detail.html', {
        'patient': patient, 'patientBloodSample_form': patientBloodSample_form, 'medications': medication_patient_doesnt_have
    })


def bloodSample_add (request, patient_id):
    form = PatientBloodSampleForm(request.POST)
    if form.is_valid():
        new_BloodSamples = form.save(commit=False)
        new_BloodSamples.patient_id = patient_id
        new_BloodSamples.save()
    return redirect('details', patient_id=patient_id)


def patient_medication(request, patient_id, medication_id):
  Patient.objects.get(id=patient_id).medications.add(medication_id)
  return redirect('details', patient_id = patient_id)


class medication_list(ListView):
  model = Medications


class medication_create(CreateView):
  model = Medications
  fields = '__all__'


class medication_update(UpdateView):
  model = Medications
  fields = ['name', 'startDate', 'endDate', 'amount']


class medication_delete(DeleteView):
  model = Medications
  success_url = '/medications/'


def bloodResult_index(request):   
    bloodSampleResults = BloodSample_Result.objects.all()
    return render(request, 'bloodResults/index.html', {'bloodSampleResults':bloodSampleResults})


def bloodResult_details(request, sample_id):
    bloodSampleResult = BloodSample_Result.objects.get (id=sample_id)
    return render(request, 'bloodResults/detail.html', {'bloodSampleResult':bloodSampleResult})

