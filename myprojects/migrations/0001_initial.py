# Generated by Django 3.2.8 on 2021-10-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(default='', max_length=150, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='pics')),
                ('startingdate', models.DateField()),
                ('endingdate', models.DateField()),
                ('techused', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
    ]
