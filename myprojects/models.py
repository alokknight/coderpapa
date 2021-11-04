from django.db import models
from django.db.models.fields import IntegerField
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import timezone
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title=models.CharField( max_length=150,primary_key=True, default="")
    img=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None)
    startingdate=models.DateField()
    endingdate=models.DateField()
    techused=models.CharField( max_length=50)
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
 

# class Profile(models.Model):
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	first_name = models.CharField(max_length=200, blank=True, null=True)
# 	last_name = models.CharField(max_length=200, blank=True, null=True)
# 	email = models.CharField(max_length=200)
# 	profile_pic = models.ImageField(null=True, blank=True, upload_to="images", default="/user.png")
# 	bio = models.TextField(null=True, blank=True)
# 	twitter = models.CharField(max_length=200,null=True, blank=True)

# 	def __str__(self):
# 		name = str(self.first_name)
# 		if self.last_name:
# 			name += ' ' + str(self.last_name)
# 		return name

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
	