# Generated by Django 3.0.7 on 2020-06-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200609_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product_model',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Laptops', 'Laptops'), ('Tabs', 'Tabs')], max_length=200, null=True),
        ),
    ]
