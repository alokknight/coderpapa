# Generated by Django 3.2.8 on 2023-11-03 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
        ('myprojects', '0007_auto_20211105_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='deploylink',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='githublink',
            field=models.URLField(unique=True),
        ),
        migrations.RemoveField(
            model_name='project',
            name='techused',
        ),
        migrations.AddField(
            model_name='project',
            name='techused',
            field=models.ManyToManyField(blank=True, to='account.Skill'),
        ),
        migrations.CreateModel(
            name='projectLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectLink', models.URLField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
