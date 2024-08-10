from django.db import models

LENGTH_TEXT_POST = 15


class Record(models.Model):
    """Модель записи."""

    name = models.TextField(
        blank=False,
        verbose_name="Наименование",
        help_text="Введите наименование",
        max_length=150
    )
    add_date = models.DateField(
        blank=False,
        auto_now_add=False,
        verbose_name="Дата поступления на склад"
    )
    storage_date = models.DateField(
        blank=False,
        auto_now_add=False,
        verbose_name="Дата хранения до"
    )
    recipient = models.TextField(
        blank=False,
        verbose_name="Заказчик",
        help_text="Введите имя заказчика",
        max_length=150
    )
    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий",
        help_text="Введите комментарий",
        max_length=150
    )

    class Meta:
        verbose_name_plural = "Записи"
        verbose_name = "Запись"
        ordering = ["add_date"]

    def __str__(self):
        name = self.name
        first_fifteen_chars = name[:LENGTH_TEXT_POST]
        return first_fifteen_chars
