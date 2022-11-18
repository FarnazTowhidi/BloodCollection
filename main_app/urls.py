from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='index'),  
    path('patients/<int:patient_id>/', views.patients_details, name='details'),  
    path('patients/create/', views.patient_create.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', views.patient_update.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', views.patients_delete.as_view(), name='patient_delete'),
    path('patients/<int:patient_id>/bloodSample_add/', views.bloodSample_add, name='bloodSample_add'),
    path('patients/<int:patient_id>/medication/<int:medication_id>/', views.patient_medication, name='patient_medication'),
    path('medication/', views.medicationList.as_view(), name='medication_index'),
    path('medication/create/', views.medication_create.as_view(), name='medication_create'),
    
    path('medication/<int:medication_id>/', views.patient_medication, name='medication_detail'),
    path('patients/<int:patient_id>/add_photo/', views.add_photo, name='add_photo'), 
    path('accounts/', include ('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'), 

]
