# Generated by Django 4.0.4 on 2022-05-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_boole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='boole',
            field=models.BooleanField(default=True),
        ),
    ]