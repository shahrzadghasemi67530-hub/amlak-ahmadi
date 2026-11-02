from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra =10


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]
    list_display = (
        "title",
        "file_code",
        "city",
        "transaction_type",
        "price",
        "created_at",
    )
    list_filter = (
        "transaction_type",
        "city",
        "parking",
        "storage",
        "elevator",
        "can_barter",
    )
    search_fields = (
        "title",
        "file_code",
        "city",
        "neighborhood",
        "street",
    )
    ordering = ("-created_at",)


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ("property", "id", "image")