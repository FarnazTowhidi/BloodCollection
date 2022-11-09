from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BloodSample_Result
from .models import Patient
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
    patientBloodSample_form = PatientBloodSampleForm()
    return render(request, 'patients/detail.html', {
        'patient': patient, 'patientBloodSample_form': patientBloodSample_form
    })


def bloodResult_index(request):   
    bloodSampleResults = BloodSample_Result.objects.all()
    return render(request, 'bloodResults/index.html', {'bloodSampleResults':bloodSampleResults})


def bloodResult_details(request, sample_id):
    bloodSampleResult = BloodSample_Result.objects.get (id=sample_id)
    return render(request, 'bloodResults/detail.html', {'bloodSampleResult':bloodSampleResult})

