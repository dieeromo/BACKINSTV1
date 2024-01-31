# Generated by Django 3.2.16 on 2024-01-29 23:07

import biblioteca.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obras',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='pdfs_biblioteca/', validators=[biblioteca.models.validate_pdf_size]),
        ),
    ]