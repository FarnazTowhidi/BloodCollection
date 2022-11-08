from django.db import models

class Sample (model.Model):
    WBC = models.IntegerField()
    RBC = models.IntegerField()
    HCT = models.IntegerField()
    MCV = models.IntegerField()
    MCH = models.IntegerField()