# Generated by Django 3.0.6 on 2020-05-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200519_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
