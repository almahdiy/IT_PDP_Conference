# Generated by Django 2.1.2 on 2018-10-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDPAPI', '0005_auto_20181017_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication',
            name='sessionID',
            field=models.CharField(max_length=250),
        ),
    ]
