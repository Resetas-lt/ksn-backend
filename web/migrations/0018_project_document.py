# Generated by Django 5.1.5 on 2025-02-06 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='project_documents', verbose_name='Dokumentas'),
        ),
    ]
