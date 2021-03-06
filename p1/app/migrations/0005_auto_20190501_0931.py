# Generated by Django 2.1.5 on 2019-05-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='hospitaldata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(max_length=50)),
                ('hospitalemail', models.EmailField(max_length=254)),
                ('EmergencyNumber', models.IntegerField()),
                ('Emergencycount', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('hospitalpassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='userdata',
            name='gender',
            field=models.CharField(max_length=128),
        ),
    ]
