from django.shortcuts import render


def landing(request):
    return render(request, "pages/landing.html")


def home(request):
    quick_contacts = [
        {
            "slug": "buy-sell",
            "title": "خرید و فروش",
            "note": "خرید، فروش و معاوضه",
            "phone_plain": "0912 225 6003",
            "phone_tel": "09122256003",
            "whatsapp": "https://wa.me/989122256003",
            "telegram": "https://t.me/USERNAME1",
            "rubika": "https://rubika.ir/USERNAME1",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "rent",
            "title": "اجاره",
            "note": "رهن، اجاره و تبدیل رهن به اجاره",
            "phone_plain": "0912 225 6004",
            "phone_tel": "09122256004",
            "whatsapp": "https://wa.me/989122256004",
            "telegram": "https://t.me/USERNAME2",
            "rubika": "https://rubika.ir/USERNAME2",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "pre-sale",
            "title": "پیش‌فروش",
            "note": "فایل‌های پیش‌فروش و پرداخت مرحله‌ای",
            "phone_plain": "0912 225 6005",
            "phone_tel": "09122256005",
            "whatsapp": "https://wa.me/989122256005",
            "telegram": "https://t.me/USERNAME3",
            "rubika": "https://rubika.ir/USERNAME3",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "partnership",
            "title": "مشارکت در ساخت",
            "note": "مشارکت، سرمایه‌گذاری و ساخت",
            "phone_plain": "0912 225 6006",
            "phone_tel": "09122256006",
            "whatsapp": "https://wa.me/989122256006",
            "telegram": "https://t.me/USERNAME4",
            "rubika": "https://rubika.ir/USERNAME4",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "barter",
            "title": "تهاتر",
            "note": "تهاتر با ملک، زمین یا آپارتمان",
            "phone_plain": "0912 225 6007",
            "phone_tel": "09122256007",
            "whatsapp": "https://wa.me/989122256007",
            "telegram": "https://t.me/USERNAME5",
            "rubika": "https://rubika.ir/USERNAME5",
            "divar": "https://divar.ir/",
        },
    ]

    specialist_contacts = [
        {
            "slug": "management",
            "title": "مدیریت",
            "note": "هماهنگی کلی و تصمیم‌گیری نهایی",
            "phone_plain": "0912 225 6001",
            "phone_tel": "09122256001",
            "whatsapp": "https://wa.me/989122256001",
            "telegram": "https://t.me/USERNAME_MGMT",
            "rubika": "https://rubika.ir/USERNAME_MGMT",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "buy-sell",
            "title": "خرید و فروش",
            "note": "مشاوره تخصصی خرید، فروش و معاوضه",
            "phone_plain": "0912 225 6002",
            "phone_tel": "09122256002",
            "whatsapp": "https://wa.me/989122256002",
            "telegram": "https://t.me/USERNAME_BUYSELL",
            "rubika": "https://rubika.ir/USERNAME_BUYSELL",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "rent",
            "title": "اجاره",
            "note": "رهن، اجاره و تبدیل",
            "phone_plain": "0912 225 6003",
            "phone_tel": "09122256003",
            "whatsapp": "https://wa.me/989122256003",
            "telegram": "https://t.me/USERNAME_RENT",
            "rubika": "https://rubika.ir/USERNAME_RENT",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "pre-sale",
            "title": "پیش‌فروش",
            "note": "پیش‌فروش و پرداخت مرحله‌ای",
            "phone_plain": "0912 225 6004",
            "phone_tel": "09122256004",
            "whatsapp": "https://wa.me/989122256004",
            "telegram": "https://t.me/USERNAME_PRESALE",
            "rubika": "https://rubika.ir/USERNAME_PRESALE",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "partnership",
            "title": "مشارکت در ساخت",
            "note": "مشارکت، ساخت و سرمایه‌گذاری",
            "phone_plain": "0912 225 6005",
            "phone_tel": "09122256005",
            "whatsapp": "https://wa.me/989122256005",
            "telegram": "https://t.me/USERNAME_PARTNERSHIP",
            "rubika": "https://rubika.ir/USERNAME_PARTNERSHIP",
            "divar": "https://divar.ir/",
        },
        {
            "slug": "barter",
            "title": "تهاتر",
            "note": "تهاتر با ملک، زمین یا آپارتمان",
            "phone_plain": "0912 225 6006",
            "phone_tel": "09122256006",
            "whatsapp": "https://wa.me/989122256006",
            "telegram": "https://t.me/USERNAME_BARTER",
            "rubika": "https://rubika.ir/USERNAME_BARTER",
            "divar": "https://divar.ir/",
        },
    ]

    return render(
        request,
        "pages/home.html",
        {
            "quick_contacts": quick_contacts,
            "specialist_contacts": specialist_contacts,
        },
    )


def customer_filters(request):
    return render(request, "pages/customer_filters.html")