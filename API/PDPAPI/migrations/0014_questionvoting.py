# Generated by Django 2.1.2 on 2018-11-06 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PDPAPI', '0013_remove_optionvoting_mcqoption_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique', models.IntegerField(default=0)),
                ('question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PDPAPI.Question')),
            ],
        ),
    ]