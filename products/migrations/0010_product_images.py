# Generated by Django 4.2.3 on 2023-07-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='products.image', verbose_name='Изображение'),
        ),
    ]