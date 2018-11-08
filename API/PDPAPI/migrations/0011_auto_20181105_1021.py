# Generated by Django 2.1.2 on 2018-11-05 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PDPAPI', '0010_auto_20181105_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalVotes', models.IntegerField(default=0)),
                ('unique', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='mac',
            name='MCQs',
        ),
        migrations.RemoveField(
            model_name='mcqoption',
            name='totalVotes',
        ),
        migrations.AddField(
            model_name='optionvoting',
            name='MCQOption_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PDPAPI.MCQOption'),
        ),
        migrations.AddField(
            model_name='optionvoting',
            name='MCQ_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PDPAPI.MCQ'),
        ),
    ]