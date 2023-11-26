from django.db import models
from django.db.models.fields import IntegerField
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import timezone
from django.contrib.auth.models import User
from account.models import Skill

class projectLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projectLink = models.URLField(unique=True)
    def __str__(self):
        return str(self.link)
    

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField( max_length=150,primary_key=True, default="")
    img=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None)
    startingdate=models.DateField()
    endingdate=models.DateField()
    techused = models.ManyToManyField(Skill, blank=True)
    githublink = models.URLField(unique=True)
    deploylink = models.URLField(unique=True)
    # desc=models.TextField()
    desc=RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True, default='www')
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.headline)
            has_slug = Project.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count) 
                has_slug = Project.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)

# class Tag(models.Model):
# 	name = models.CharField(max_length=200)

# 	def __str__(self):
# 		return self.name



# class ProjectComment(models.Model):
# 	author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
# 	post = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
# 	body = models.TextField(null=True, blank=True)
# 	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

# 	def __str__(self):
# 		return self.body

# 	@property
# 	def created_dynamic(self):
# 		now = timezone.now()
# 		return now
	