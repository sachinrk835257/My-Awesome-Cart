# Generated by Django 4.1.7 on 2023-06-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_youritems'),
    ]

    operations = [
        migrations.CreateModel(
            name='yourCart',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='yourItems',
        ),
    ]
