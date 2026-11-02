from django.db import models
from django.utils import timezone


class Property(models.Model):
    class TransactionType(models.TextChoices):
        BUY = "buy", "خرید"
        SELL = "sell", "فروش"
        RENT = "rent", "اجاره"
        RENT_SALE = "rent_sale", "رهن و اجاره"
        PRE_SALE = "pre_sale", "پیش‌فروش"
        PARTNERSHIP = "partnership", "مشارکت در ساخت"
        BARTER = "barter", "تهاتر"

    class Direction(models.TextChoices):
        NORTH = "north", "شمالی"
        SOUTH = "south", "جنوبی"
        EAST = "east", "شرقی"
        WEST = "west", "غربی"

    class UnitType(models.TextChoices):
        SINGLE = "single", "تک واحدی"
        TWO_UNIT = "two_unit", "دو واحدی"
        MULTI = "multi", "چند واحدی"
        WHOLE = "whole", "کل ملک"

    class DeedType(models.TextChoices):
        OFFICIAL = "official", "سند رسمی"
        SINGLE_PAGE = "single_page", "تک برگ"
        CONTRACTUAL = "contractual", "قولنامه‌ای"
        OTHER = "other", "سایر"

    title = models.CharField("عنوان ملک", max_length=200)
    file_code = models.CharField("کد فایل", max_length=50, unique=True)

    city = models.CharField("شهر", max_length=100)
    neighborhood = models.CharField("محله", max_length=150, blank=True)
    street = models.CharField("خیابان", max_length=150, blank=True)

    transaction_type = models.CharField(
        "نوع معامله",
        max_length=20,
        choices=TransactionType.choices,
        default=TransactionType.BUY,
    )

    direction = models.CharField(
        "جهت ملک",
        max_length=10,
        choices=Direction.choices,
        blank=True,
    )

    unit_type = models.CharField(
        "نوع واحد",
        max_length=20,
        choices=UnitType.choices,
        blank=True,
    )

    area = models.PositiveIntegerField("متراژ", null=True, blank=True)
    price = models.BigIntegerField("قیمت", null=True, blank=True)
    deposit = models.BigIntegerField("مبلغ رهن", null=True, blank=True)
    rent = models.BigIntegerField("مبلغ اجاره", null=True, blank=True)

    bedrooms = models.PositiveSmallIntegerField("تعداد خواب", null=True, blank=True)
    floor = models.PositiveSmallIntegerField("طبقه", null=True, blank=True)
    total_floors = models.PositiveSmallIntegerField("تعداد طبقات", null=True, blank=True)
    units_per_floor = models.PositiveSmallIntegerField("تعداد واحد در طبقه", null=True, blank=True)

    year_built = models.PositiveSmallIntegerField("سال ساخت", null=True, blank=True)

    parking = models.BooleanField("پارکینگ", default=False)
    storage = models.BooleanField("انباری", default=False)
    elevator = models.BooleanField("آسانسور", default=False)
    yard = models.BooleanField("حیاط", default=False)
    balcony = models.BooleanField("بالکن", default=False)

    deed_type = models.CharField(
        "نوع سند",
        max_length=20,
        choices=DeedType.choices,
        blank=True,
    )

    is_single_unit = models.BooleanField("تک واحدی", default=False)

    can_barter = models.BooleanField("قابل تهاتر", default=False)
    barter_preference = models.CharField("ترجیح تهاتر", max_length=150, blank=True)
    barter_note = models.TextField("توضیحات تهاتر", blank=True)

    description = models.TextField("توضیحات", blank=True)
    created_at = models.DateTimeField("تاریخ ثبت", default=timezone.now)

    class Meta:
        verbose_name = "ملک"
        verbose_name_plural = "فایل‌های املاک"

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        related_name="images",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="properties/")

    class Meta:
        verbose_name = "عکس ملک"
        verbose_name_plural = "عکس‌های ملک"

    def __str__(self):
        return f"{self.property.title} - تصویر {self.id}"