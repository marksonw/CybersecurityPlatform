# Generated by Django 4.0.1 on 2022-02-05 00:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('research_title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=2500, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
