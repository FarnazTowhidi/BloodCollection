# Generated by Django 4.1.3 on 2022-11-10 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_rename_bloodsample_result_bloodsampleresult_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='medications',
            field=models.ManyToManyField(to='main_app.medications'),
        ),
    ]
