# Generated by Django 2.2.3 on 2019-07-25 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190725_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='script',
            name='script_name',
        ),
    ]
