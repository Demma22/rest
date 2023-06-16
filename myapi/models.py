from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    residence = models.CharField(max_length=60, null=True)
    dob = models.DateField(max_length=150, null=True)
    def __str__(self):
        return self.name 