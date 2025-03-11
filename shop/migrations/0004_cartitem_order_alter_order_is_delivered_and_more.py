# Generated by Django 5.1.6 on 2025-03-05 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_remove_cartitem_order_alter_book_img_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="order",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="shop.order"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="is_delivered",
            field=models.BooleanField(default=False, verbose_name="Доставлен?"),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата создания заказа"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(max_length=20, verbose_name="Статус заказа"),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(max_length=20, verbose_name="Способ оплаты"),
        ),
        migrations.AlterField(
            model_name="order",
            name="total_cost",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Стоимость заказа"
            ),
        ),
    ]
