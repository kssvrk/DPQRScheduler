# Generated by Django 2.2.3 on 2019-07-25 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='schedule_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
