# Generated by Django 4.2.6 on 2023-10-10 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_rename_category_product_category_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]