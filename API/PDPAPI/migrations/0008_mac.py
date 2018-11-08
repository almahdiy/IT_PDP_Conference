# Generated by Django 2.1.2 on 2018-11-04 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PDPAPI', '0007_mcq_mcqoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='MAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.IntegerField(default=0)),
                ('MCQ_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PDPAPI.MCQ')),
            ],
        ),
    ]