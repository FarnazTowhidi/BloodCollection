from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='index'),  
    path('patients/<int:patient_id>/', views.patients_details, name='details'),  
    path('patients/<int:pk>/update/', views.patientUpdate.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', views.patientsDelete.as_view(), name='patient_delete'),
    path('patients/<int:patient_id>/bloodSample_add/', views.bloodSample_add, name='bloodSample_add')

    
]
