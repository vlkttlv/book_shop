# Generated by Django 5.1.6 on 2025-03-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0010_order_updated_at_alter_order_order_status_orderitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="img",
            field=models.ImageField(upload_to="img/", verbose_name="Изображение"),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="id",
            field=models.AutoField(
                primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
