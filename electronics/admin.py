from django.contrib import admin
from .models import Supplier, NetworkNode, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'debt_to_supplier', 'created_at')


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'level', 'debt_to_supplier', 'created_at')
    list_filter = ('city', 'country')
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0.00)

    clear_debt.short_description = 'Очистить задолженность перед поставщиком'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
