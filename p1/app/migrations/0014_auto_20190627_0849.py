# Generated by Django 2.1.5 on 2019-06-27 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190627_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitaldata2',
            name='hospitalname',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='app.hospitaldata'),
        ),
    ]
