# Generated by Django 3.0.5 on 2022-03-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='crud/images')),
            ],
        ),
    ]
