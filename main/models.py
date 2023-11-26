from django.db import models
from django.db.models.fields import IntegerField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122, default="")
    email=models.EmailField(max_length=122,primary_key=True)
    phone=models.BigIntegerField()
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name



class Tutorial(models.Model):
    id=models.IntegerField(primary_key=True,default="")
    subject=models.CharField( default="xyz",max_length=100)
    img=models.ImageField( upload_to="images",height_field=None, width_field=None, max_length=None)
    sampleLink = models.URLField(blank=True, null=True )
    desc=RichTextUploadingField()
    price=models.IntegerField()
    offer=models.BooleanField()
    slug = models.SlugField(null=True, blank=True, default='tutorial')

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.headline)
            has_slug = Tutorial.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count) 
                has_slug = Tutorial.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)

class FrontPage(models.Model):
    title=models.CharField( primary_key=True,max_length=100,default=0)
    desc=models.CharField(max_length=150,default="")
    img=models.CharField(max_length=30,default="")
    minRead=models.IntegerField()
    def __str__(self):
        return self.title


class Crausal(models.Model):
    id=models.IntegerField(primary_key=True,default=0)
    title=models.CharField( max_length=50)
    img1=models.ImageField( upload_to='images', height_field=None, width_field=None, max_length=None)
    img2=models.CharField(max_length=50,default="mountain")
    ctext=models.CharField(max_length=100)
    def __str__(self):
        return self.title

