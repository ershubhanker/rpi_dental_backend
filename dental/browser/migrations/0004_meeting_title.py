# Generated by Django 5.1.3 on 2024-12-07 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_remove_meeting_patient_name_meeting_patient_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
