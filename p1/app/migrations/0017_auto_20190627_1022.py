# Generated by Django 2.1.5 on 2019-06-27 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190627_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitaldata2',
            name='hospitalname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hospitaldata'),
        ),
    ]
