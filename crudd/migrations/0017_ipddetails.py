# Generated by Django 3.0.5 on 2022-03-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudd', '0016_opddetails_odate'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPDDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=50)),
                ('idate', models.CharField(max_length=50)),
                ('iaddress', models.CharField(max_length=300)),
                ('iphone', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'IPD Details',
            },
        ),
    ]
