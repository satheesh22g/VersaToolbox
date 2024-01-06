# Generated by Django 5.0 on 2023-12-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('encrypted_password', models.CharField(max_length=128)),
            ],
        ),
    ]