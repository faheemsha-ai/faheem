# Generated by Django 4.1 on 2024-09-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_cartitem_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.CharField(blank=True, choices=[('Electronics', 'Electronics'), ('Groccery', 'Groccery'), ('Fruit', 'Fruit'), ('Vegitables', 'Vegitbales')], max_length=20),
        ),
    ]
