# Generated by Django 5.1.5 on 2025-02-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_rename_projectfiles_projectfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='Balsuotojo IP')),
                ('rating', models.CharField(choices=[('perfect', 'Puikiai'), ('good', 'Gerai'), ('decent', 'Patenkinamai'), ('bad', 'Blogai')], max_length=100, verbose_name='Įvertinimas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')),
            ],
            options={
                'verbose_name': 'Įvertinimas',
                'verbose_name_plural': 'Įvertinimai',
            },
        ),
    ]
