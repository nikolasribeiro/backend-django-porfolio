# Generated by Django 3.1.7 on 2021-08-18 22:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210329_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='long_blog_description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='porfolio',
            name='long_description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]