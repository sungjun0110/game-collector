# Generated by Django 4.0.1 on 2022-01-15 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_playhistory_options_remove_release_game_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='release',
            old_name='name',
            new_name='platform',
        ),
        migrations.RemoveField(
            model_name='release',
            name='release_date',
        ),
    ]
