# Generated by Django 3.0.5 on 2022-03-27 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudd', '0005_auto_20220327_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeedetails',
            options={'verbose_name_plural': 'Employee Details'},
        ),
        migrations.AlterModelOptions(
            name='patientdetails',
            options={'verbose_name_plural': 'Patient Details'},
        ),
    ]
