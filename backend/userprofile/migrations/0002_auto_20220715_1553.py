# Generated by Django 2.2.5 on 2022-07-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
