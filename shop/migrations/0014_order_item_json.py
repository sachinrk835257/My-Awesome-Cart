# Generated by Django 4.1.7 on 2023-06-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_order_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item_json',
            field=models.CharField(default=' ', max_length=5000),
        ),
    ]
