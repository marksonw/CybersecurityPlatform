# Generated by Django 4.0.1 on 2022-02-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0009_research_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='research_description',
            field=models.TextField(blank=True),
        ),
    ]
