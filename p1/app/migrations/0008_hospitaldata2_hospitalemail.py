# Generated by Django 2.1.5 on 2019-05-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_hospitaldata2'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitaldata2',
            name='hospitalemail',
            field=models.EmailField(default='null', max_length=254),
            preserve_default=False,
        ),
    ]
