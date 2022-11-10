from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient
from .models import BloodSamples
from .models import Medications
from .models import BloodSampleResult 
from .forms import PatientBloodSampleForm

class patientUpdate(UpdateView):
    model = Patient
    fields = '__all__'
    patients = Patient.objects.all()
    success_url = "/patients"


class patientsDelete(DeleteView):
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

def bloodResult_index(request):   
    bloodSampleResults = BloodSample_Result.objects.all()
    return render(request, 'bloodResults/index.html', {'bloodSampleResults':bloodSampleResults})


def bloodResult_details(request, sample_id):
    bloodSampleResult = BloodSample_Result.objects.get (id=sample_id)
    return render(request, 'bloodResults/detail.html', {'bloodSampleResult':bloodSampleResult})

