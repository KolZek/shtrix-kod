# Generated by Django 5.1 on 2024-08-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0009_record_volume_record_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="volume",
            field=models.FloatField(
                help_text="Введите объем в м³", verbose_name="Объем"
            ),
        ),
        migrations.AlterField(
            model_name="record",
            name="weight",
            field=models.FloatField(
                help_text="Введите вес в килограммах", verbose_name="Вес"
            ),
        ),
    ]