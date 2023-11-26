from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from account.models import Skill
# Create your models here.
class Tutorial(models.Model):
    id=models.IntegerField(primary_key=True,default="")
    subject = models.ManyToManyField(Skill, blank=True)
    title = models.CharField(max_length=200)
    img=models.ImageField( upload_to="images",height_field=None, width_field=None, max_length=None)
    sampleLink = models.URLField(blank=True, null=True )
    desc=RichTextUploadingField()
    price=models.IntegerField()
    offer=models.BooleanField()
    slug = models.SlugField(null=True, blank=True, default='tutorial')

    def __str__(self):
        return str(self.title)

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