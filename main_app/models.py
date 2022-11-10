from django.db import models

class Medications(models.Model):
    name = models.CharField(max_length=200)
    startDate= models.DateField()
    endDate = models.DateField()
    amount = models.IntegerField()


class Patient (models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    sex = models.CharField(max_length = 4)
    HealthCareNumber = models.IntegerField()
    familyDoctor = models.CharField(max_length = 100, default="Dr. Martin")
    medications = models.ManyToManyField(Medications)


class BloodSamples (models.Model):   
    collectionDate = models.DateField()
    orderingPhysician = models.CharField(max_length = 100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=1)


class BloodSampleResult (models.Model):
    WBC = models.DecimalField(max_digits=5, decimal_places=1)
    RBC = models.DecimalField(max_digits=5, decimal_places=1)
    HCT = models.DecimalField(max_digits=5, decimal_places=1)
    MCV = models.DecimalField(max_digits=5, decimal_places=1)
    MCH = models.DecimalField(max_digits=5, decimal_places=1)
    Lymphocyte = models.DecimalField(max_digits=5, decimal_places=1)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1 )

