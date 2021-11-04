from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Wine(models.Model):
    brand=models.CharField(max_length=100,primary_key=True)
    img=models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)
    mfgDate=models.DateField()
    price=models.IntegerField()
    offer=models.BooleanField()

    def __str__(self):
        return self.brand

