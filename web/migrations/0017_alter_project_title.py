# Generated by Django 5.1.5 on 2025-02-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Pavadinimas'),
        ),
    ]
