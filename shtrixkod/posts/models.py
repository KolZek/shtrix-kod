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
    marking = models.CharField(
        blank=False,
        verbose_name="Маркировка",
        help_text="Введите маркировку",
        max_length=30
    )
    amount = models.IntegerField(
        blank=False,
        verbose_name="Количество мест",
        help_text="Введите количество мест"
    )
    weight = models.FloatField(
        blank=False,
        verbose_name="Вес",
        help_text="Введите вес в килограммах"
    )
    volume = models.FloatField(
        blank=False,
        verbose_name="Объем",
        help_text="Введите объем в м³"
    )
    add_date = models.DateField(
        blank=False,
        auto_now_add=False,
        verbose_name="Дата поступления на склад"
    )
    issue_date = models.DateField(
        blank=True, null=True,
        auto_now_add=False,
        verbose_name="Дата выдачи"
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
        ordering = ["issue_date", "-add_date"]

    def __str__(self):
        name = self.name
        first_fifteen_chars = name[:LENGTH_TEXT_POST]
        return first_fifteen_chars
