# Generated by Django 3.0.5 on 2022-03-30 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudd', '0008_auto_20220329_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=50)),
                ('demail', models.CharField(max_length=50)),
                ('dspecialist', models.CharField(max_length=300)),
                ('dphone', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Doctor Details',
            },
        ),
    ]
