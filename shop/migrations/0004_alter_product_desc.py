# Generated by Django 4.1.7 on 2023-06-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_subcategory_product_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=600),
        ),
    ]
