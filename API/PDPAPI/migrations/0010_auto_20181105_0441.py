# Generated by Django 2.1.2 on 2018-11-05 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PDPAPI', '0009_auto_20181104_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mac',
            old_name='MCQ_id',
            new_name='MCQs',
        ),
    ]
