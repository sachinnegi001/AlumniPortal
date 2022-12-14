# Generated by Django 4.0.3 on 2022-05-20 18:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('jobrole', models.CharField(max_length=200)),
                ('companyname', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('discription', models.TextField(blank=True, null=True)),
                ('source_link', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
