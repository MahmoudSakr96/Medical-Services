# Generated by Django 2.1.5 on 2019-06-27 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20190627_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitaldata2',
            name='hospitalname',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='app.hospitaldata'),
        ),
    ]
