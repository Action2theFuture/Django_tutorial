# Generated by Django 3.2 on 2021-04-29 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210429_0402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='runnig_time',
            new_name='running_time',
        ),
    ]
