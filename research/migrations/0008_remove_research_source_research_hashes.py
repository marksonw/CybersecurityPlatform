# Generated by Django 4.0.1 on 2022-02-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0007_alter_research_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='source',
        ),
        migrations.AddField(
            model_name='research',
            name='hashes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
