# Generated by Django 5.1.5 on 2025-02-06 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_project_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='document',
        ),
        migrations.CreateModel(
            name='ProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='project_files', verbose_name='Failas')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='web.project')),
            ],
            options={
                'verbose_name': 'Projekto failas',
                'verbose_name_plural': 'Projektų failai',
            },
        ),
    ]
