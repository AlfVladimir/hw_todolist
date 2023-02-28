from django.contrib import admin
from .models import Tasklist

# Register your models here.


@admin.register(Tasklist)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "is_done",
        "timestamp_create",
        "timestamp_done",
    )
    list_filter = ["is_done", "timestamp_create"]
    search_fields = ["text"]
