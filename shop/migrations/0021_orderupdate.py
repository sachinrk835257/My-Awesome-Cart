# Generated by Django 4.1.7 on 2023-06-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_delete_orderupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('item_json', models.CharField(default='not given', max_length=1000)),
                ('email', models.CharField(max_length=111)),
                ('update_desc', models.CharField(max_length=5000)),
                ('timeStamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]