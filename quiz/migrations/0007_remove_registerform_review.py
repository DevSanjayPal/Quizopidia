# Generated by Django 4.1.2 on 2022-11-08 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_studentreport_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerform',
            name='review',
        ),
    ]
