from django.db import models

# Create your models here.
class Vessel(models.Model):
    name = models.CharField(max_length=50)
    company_id = models.CharField(max_length=100)
    NACCS_code = models.CharField(max_length=100, unique=True)