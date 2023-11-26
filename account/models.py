from django.db import models
from django.contrib.auth.models import User,auth

class Skill(models.Model):
    skillname = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.skillname

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    skills = models.ManyToManyField(Skill, blank=True)
    dp = models.ImageField(upload_to="pics")
    phone = models.BigIntegerField(null=True, default=None)
    profession = models.CharField(max_length=50, null=True, default=None)
    experience = models.CharField(max_length=50, null=True, default=None)
    rate = models.IntegerField(null=True, default=None)
    eng_level = models.CharField(max_length=10, null=True, default=None)
    completedProjectNo = models.IntegerField(null=True, default=None)
    availability = models.IntegerField(null=True, default=None)
    bio = models.TextField(null=True, default=None)  # Changed to TextField for longer text
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.user.username
    
    # def __str__(self):
    #     name = str(self.user.first_name)
    #     if self.user.last_name:
    #         name += ' ' + str(self.user.last_name)
    #     return name