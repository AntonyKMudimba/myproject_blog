# Generated by Django 3.2.6 on 2021-08-06 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='details',
        ),
    ]
