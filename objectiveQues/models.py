from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Ques(models.Model):
    quesno  =models.BigIntegerField(primary_key=True,default='00')
    ques    =RichTextUploadingField()
    option1 =models.CharField(max_length=100)
    option2 =models.CharField(max_length=100)
    option3 =models.CharField(max_length=100)
    option4 =models.CharField(max_length=100)
    ans =models.CharField(max_length=10)
    exp =models.CharField(max_length=300)
    def __str__(self):
        s=self.ques
        print(s)
        return str(self.quesno)
        


class Subject(models.Model):
    ques= models.ForeignKey(Ques, on_delete=models.CASCADE)
    subject=models.CharField(default="", max_length=50)
    def __str__(self):
        return self.subject
