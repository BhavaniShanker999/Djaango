# Generated by Django 3.0.7 on 2020-06-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_product_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_model',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Laptops', 'Lappy'), ('Tabs', 'Tabs')], max_length=200, null=True),
        ),
    ]
