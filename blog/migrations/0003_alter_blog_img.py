# Generated by Django 3.2.8 on 2021-10-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
