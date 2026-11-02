from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Property

def property_list(request):
    qs = Property.objects.all().order_by("-id")

    # نوع معامله
    transaction_type = request.GET.get("transaction_type")
    if transaction_type:
        qs = qs.filter(transaction_type=transaction_type)

    # شهر
    city = request.GET.get("city")
    if city:
        qs = qs.filter(city__icontains=city)

    # محله
    neighborhood = request.GET.get("neighborhood")
    if neighborhood:
        qs = qs.filter(neighborhood__icontains=neighborhood)

    # خیابان
    street = request.GET.get("street")
    if street:
        qs = qs.filter(street__icontains=street)

    # حداقل متراژ
    min_area = request.GET.get("min_area")
    if min_area:
        qs = qs.filter(area__gte=min_area)

    # حداکثر متراژ
    max_area = request.GET.get("max_area")
    if max_area:
        qs = qs.filter(area__lte=max_area)

    # حداقل قیمت
    min_price = request.GET.get("min_price")
    if min_price:
        qs = qs.filter(price__gte=min_price)

    # حداکثر قیمت
    max_price = request.GET.get("max_price")
    if max_price:
        qs = qs.filter(price__lte=max_price)

    # جهت
    direction = request.GET.get("direction")
    if direction:
        qs = qs.filter(direction=direction)

    # تعداد خواب
    bedrooms = request.GET.get("bedrooms")
    if bedrooms:
        qs = qs.filter(bedrooms=bedrooms)

    # امکانات
    if request.GET.get("parking"):
        qs = qs.filter(parking=True)

    if request.GET.get("storage"):
        qs = qs.filter(storage=True)

    if request.GET.get("elevator"):
        qs = qs.filter(elevator=True)

    if request.GET.get("yard"):
        qs = qs.filter(yard=True)

    if request.GET.get("balcony"):
        qs = qs.filter(balcony=True)

    if request.GET.get("barter"):
        qs = qs.filter(can_barter=True)

    paginator = Paginator(qs, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "properties/property_list.html",
        {
            "properties": page_obj,
        },
    )


def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)

    return render(
        request,
        "properties/property_detail.html",
        {
            "property": property,
        },
    )