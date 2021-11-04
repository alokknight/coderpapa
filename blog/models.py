# Create your models here.
# # from django import forms
# from django.db.models.fields import IntegerField
# from ckeditor.fields import RichTextField
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100,primary_key=True)
    img=models.ImageField(upload_to="uploads", height_field=None, width_field=None, max_length=None,blank=True)
    img2=models.CharField(max_length=50,default='sunset,girl')
    # desc=RichTextField()
    desc=RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True, default='blog')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.headline)
            has_slug = Blog.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count) 
                has_slug = Blog.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)
