# Generated by Django 3.2.8 on 2023-11-04 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objectiveQues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='ques',
        ),
        migrations.AddField(
            model_name='ques',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='objectiveQues.subject'),
        ),
    ]
