# Generated by Django 4.1.3 on 2022-11-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WBC', models.IntegerField()),
                ('RBC', models.IntegerField()),
                ('HCT', models.IntegerField()),
                ('MCV', models.IntegerField()),
                ('MCH', models.IntegerField()),
            ],
        ),
    ]