# Generated by Django 4.0.3 on 2022-08-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0009_studentprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='rollnumber',
            field=models.IntegerField(null=True),
        ),
    ]