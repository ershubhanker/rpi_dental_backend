# Generated by Django 5.1.3 on 2024-11-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Discharged', 'Discharged')], default='Active', max_length=10, null=True)),
            ],
        ),
    ]
