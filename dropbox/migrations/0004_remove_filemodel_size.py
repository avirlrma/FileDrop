# Generated by Django 3.0.5 on 2020-04-10 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dropbox', '0003_filemodel_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filemodel',
            name='size',
        ),
    ]
