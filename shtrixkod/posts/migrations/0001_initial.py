# Generated by Django 5.1 on 2024-08-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="Введите наименование", verbose_name="Наименование"
                    ),
                ),
                (
                    "add_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата поступления на склад"
                    ),
                ),
                ("storage_date", models.DateTimeField(verbose_name="Дата хранения до")),
                (
                    "recipient",
                    models.TextField(
                        help_text="Введите имя заказчика", verbose_name="Заказчик"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="Введите комментарий",
                        verbose_name="Комментарий",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
                "ordering": ["-add_date"],
            },
        ),
    ]
