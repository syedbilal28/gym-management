# Generated by Django 4.0.1 on 2022-01-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_alter_service_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]