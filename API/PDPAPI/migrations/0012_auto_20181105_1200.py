# Generated by Django 2.1.2 on 2018-11-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDPAPI', '0011_auto_20181105_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionvoting',
            name='totalVotes',
        ),
        migrations.AddField(
            model_name='mcqoption',
            name='totalVotes',
            field=models.IntegerField(default=0),
        ),
    ]
