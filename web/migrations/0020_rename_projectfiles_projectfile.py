# Generated by Django 5.1.5 on 2025-02-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_remove_project_document_projectfiles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectFiles',
            new_name='ProjectFile',
        ),
    ]
