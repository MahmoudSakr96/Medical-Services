# Generated by Django 2.1.5 on 2019-06-27 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20190627_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitaldata2',
            name='hospitalname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hospitaldata'),
        ),
    ]
