# Generated by Django 3.0.3 on 2020-05-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendormod',
            name='AdharCard',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vendormod',
            name='Age',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vendormod',
            name='PhoneNo',
            field=models.CharField(max_length=30),
        ),
    ]