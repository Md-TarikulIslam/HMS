# Generated by Django 3.0.5 on 2022-03-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudd', '0017_ipddetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opddetails',
            name='odate',
            field=models.CharField(max_length=50),
        ),
    ]