# Generated by Django 5.0 on 2024-01-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_errorreport_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorreport',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='error_screenshots/'),
        ),
    ]
