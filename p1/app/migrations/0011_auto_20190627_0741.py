# Generated by Django 2.1.5 on 2019-06-27 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190617_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitaldata2',
            name='hospitalemail',
        ),
        migrations.RemoveField(
            model_name='hospitaldata2',
            name='hospitalpassword',
        ),
    ]
