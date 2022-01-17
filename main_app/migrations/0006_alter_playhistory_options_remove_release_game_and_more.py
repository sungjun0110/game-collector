# Generated by Django 4.0.1 on 2022-01-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_playhistory_playtime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playhistory',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='release',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='releases',
            field=models.ManyToManyField(to='main_app.Release'),
        ),
    ]
