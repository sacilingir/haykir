# Generated by Django 5.0.3 on 2024-04-25 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haykirapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='mesage',
            new_name='message',
        ),
    ]
