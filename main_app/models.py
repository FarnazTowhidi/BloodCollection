from django.db import models

# Create your models here.
class Sample (models.Model):
    WBC = models.IntegerField()
    RBC = models.IntegerField()
    HCT = models.IntegerField()
    MCV = models.IntegerField()
    MCH = models.IntegerField()
    Lymphocyte = models.IntegerField()
    

class Patient (models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    sex = models.BinaryField()


