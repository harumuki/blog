# Generated by Django 2.0.13 on 2019-09-14 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190914_0727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpagetag',
            old_name='content',
            new_name='content_object',
        ),
    ]