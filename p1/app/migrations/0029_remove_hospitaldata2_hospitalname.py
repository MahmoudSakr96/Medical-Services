# Generated by Django 2.1.5 on 2019-06-27 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20190627_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitaldata2',
            name='hospitalname',
        ),
    ]
