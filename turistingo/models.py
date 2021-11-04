from django.db import models

# Create your models here.
class Turistingo(models.Model):
    city=models.CharField( max_length=100,primary_key=True, default="")
    img=models.ImageField( upload_to="images", height_field=None, width_field=None, max_length=None)
    desc=models.TextField()
    price=models.IntegerField(default=10000)
    dis=models.IntegerField(default=00)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.city