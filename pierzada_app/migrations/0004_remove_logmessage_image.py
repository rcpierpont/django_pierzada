# Generated by Django 5.0.4 on 2024-06-01 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pierzada_app', '0003_alter_logmessage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logmessage',
            name='image',
        ),
    ]
