from django.urls import path
from .views import landing, home, customer_filters

urlpatterns = [
    path("", landing, name="landing"),
    path("home/", home, name="home"),
    path("customers/", customer_filters, name="customer_filters"),
]