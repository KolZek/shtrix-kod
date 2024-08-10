from django.contrib import admin

from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    """Регистрация модели записей в админке."""

    list_display = ("pk", "name", "add_date", "storage_date", "recipient", "comment")
    search_fields = ("name", "recipient")
    list_filter = ("add_date", "storage_date")
    empty_value_display = "-пусто-"
