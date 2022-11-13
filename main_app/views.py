from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Patient, BloodSamples, Medications, BloodSampleResult , Photo
from .forms import PatientBloodSampleForm

import boto3
import uuid

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'gacatcollectordjango'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def add_photo(request, patient_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, patient_id=patient_id)
      print (photo)
      photo.save()
    except Exception as e:
      print (e)
      print("An error occurred uploading file to s3")
    
  return redirect('details', patient_id=patient_id)


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


class medicationList(ListView):
  model = Medications
  # template_name = "medication_List.html"
  # context_object_name="medication"


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

