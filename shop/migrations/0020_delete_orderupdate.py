# Generated by Django 4.1.7 on 2023-06-28 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_orderupdate_timestamp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='orderUpdate',
        ),
    ]
