# Generated by Django 4.0.1 on 2022-03-01 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0011_remove_research_hashes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='research',
            old_name='research_description',
            new_name='description',
        ),
    ]
