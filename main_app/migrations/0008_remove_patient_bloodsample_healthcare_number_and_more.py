# Generated by Django 4.1.3 on 2022-11-09 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_delete_patient_prescription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_bloodsample',
            name='HealthCare_number',
        ),
        migrations.AddField(
            model_name='patient',
            name='HealthCare_number',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
