from django.db import models


class Patient (models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    sex = models.CharField(max_length = 4)
    HealthCare_number = models.IntegerField()
    family_doctor = models.CharField(max_length = 100, default="Dr. Martin")


class Patient_BloodSample (models.Model):   
    collection_date = models.DateField()
    ordering_Physician = models.CharField(max_length = 100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=1)


class BloodSample_Result (models.Model):
    WBC = models.DecimalField(max_digits=5, decimal_places=1)
    RBC = models.DecimalField(max_digits=5, decimal_places=1)
    HCT = models.DecimalField(max_digits=5, decimal_places=1)
    MCV = models.DecimalField(max_digits=5, decimal_places=1)
    MCH = models.DecimalField(max_digits=5, decimal_places=1)
    Lymphocyte = models.DecimalField(max_digits=5, decimal_places=1)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1 )


# class Patient_Prescription (models.Model):
#     name = models.CharField(max_length = 100)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     amount = models.IntegerField()
#     Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)



