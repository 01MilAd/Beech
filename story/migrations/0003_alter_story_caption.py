# Generated by Django 3.2.7 on 2021-10-02 01:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20210926_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='caption',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True),
        ),
    ]
