# Generated by Django 3.1.3 on 2021-06-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20210610_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]