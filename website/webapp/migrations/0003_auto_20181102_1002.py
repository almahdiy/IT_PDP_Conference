# Generated by Django 2.1.2 on 2018-11-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.CharField(max_length=1000),
        ),
    ]
