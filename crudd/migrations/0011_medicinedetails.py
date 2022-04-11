# Generated by Django 3.0.5 on 2022-03-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudd', '0010_salarydetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=50)),
                ('mstock', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'Medicine Details',
            },
        ),
    ]
