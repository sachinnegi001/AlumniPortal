# Generated by Django 4.0.3 on 2022-06-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_posteventform_last_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteventform',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
    ]