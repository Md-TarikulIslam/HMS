# Generated by Django 3.0.5 on 2022-03-30 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudd', '0009_doctordetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('saccountno', models.CharField(max_length=50)),
                ('smonth', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Salary Details',
            },
        ),
    ]