# Generated by Django 5.1.6 on 2025-03-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_remove_cartitem_order_order_cart_items"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="cartitem",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=50
            ),
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
