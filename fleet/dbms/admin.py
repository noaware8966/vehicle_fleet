from django.contrib import admin

from .models import Client, PickupPoint, Car, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    search_fields = ('full_name',)


@admin.register(PickupPoint)
class PickupPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
    search_fields = ('address',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'license_plate')
    search_fields = ('brand', 'license_plate')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number_order', 'client', 'delivery_date', 'payment_date', 'amount')
    list_display_links = ('number_order',)
    list_filter = ('delivery_date', 'payment_date')
    search_fields = ('client__full_name',)
