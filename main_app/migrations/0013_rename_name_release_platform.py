# Generated by Django 4.0.1 on 2022-01-17 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_release_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='release',
            old_name='name',
            new_name='platform',
        ),
    ]
