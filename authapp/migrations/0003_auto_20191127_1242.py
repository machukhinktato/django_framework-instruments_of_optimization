# Generated by Django 2.2.5 on 2019-11-27 09:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20191125_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 29, 9, 42, 47, 476222, tzinfo=utc)),
        ),
    ]