# Generated by Django 4.0.3 on 2022-05-16 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_rename_user_profile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]