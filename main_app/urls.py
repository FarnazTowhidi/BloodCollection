from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('samples/', views.sample_index, name='index'),  
    path('samples/<int:sample_id>', views.sample_details, name='detail',)
]
