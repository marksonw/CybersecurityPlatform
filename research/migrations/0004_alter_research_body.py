# Generated by Django 4.0.1 on 2022-02-15 20:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_rename_description_research_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
