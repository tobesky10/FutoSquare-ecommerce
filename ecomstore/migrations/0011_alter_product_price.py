# Generated by Django 4.0.2 on 2022-04-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomstore', '0010_alter_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
