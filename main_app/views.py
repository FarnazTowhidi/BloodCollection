from django.shortcuts import render
from .models import Sample

# samples = [
#     sample(6.9, 1.8, 19.5, 109.6, 31 ),
#     sample(5.2, 3.51, 41.5, 117.6, 27 ),
#     sample(6.5, 5.01, 31.3, 90.2, 45 ),
# ]

def home(request):
  return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def sample_index(request):
    
    samples = Sample.objects.all()
    return render(request, 'samples/index.html', {'samples':samples})

def sample_details(request, sample_id):
    sample = Sample.objects.get (id=sample_id)
    return render(request, 'samples/detail.html', {'sample':sample})

