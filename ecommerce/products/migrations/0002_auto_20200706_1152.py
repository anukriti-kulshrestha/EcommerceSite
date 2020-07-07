# Generated by Django 3.0.2 on 2020-07-06 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('shipping_address', models.CharField(max_length=100)),
                ('order_address', models.CharField(max_length=100)),
                ('order_email', models.EmailField(max_length=254)),
                ('order_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('E', 'Electronics'), ('F', 'Fashion'), ('B', 'Books'), ('H', 'Household')], max_length=100),
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem_price', to='products.Product')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Orders')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem_prod_id', to='products.Product')),
            ],
        ),
    ]
