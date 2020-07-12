# Generated by Django 3.0.7 on 2020-06-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200609_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product_model',
            name='category',
            field=models.CharField(choices=[('Astro', 'Astro'), ('Amazon', 'Amazon'), ('Mobiles', 'Mobiles'), ('Laptops', 'Laptops'), ('Tabs', 'Tabs')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product_model',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag_model'),
        ),
    ]
