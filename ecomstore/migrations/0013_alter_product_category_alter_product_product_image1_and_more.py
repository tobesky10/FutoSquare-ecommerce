# Generated by Django 4.0.2 on 2022-05-27 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomstore', '0012_remove_product_product_image_product_product_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomstore.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]