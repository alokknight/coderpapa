# Generated by Django 3.2.8 on 2021-11-03 22:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0005_alter_project_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
