# Generated by Django 2.2.8 on 2020-06-22 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('loc_x', models.DecimalField(decimal_places=6, max_digits=10)),
                ('loc_y', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='KeyVal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('locname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Warehouse')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
    ]
