# Generated by Django 4.0.1 on 2022-01-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]