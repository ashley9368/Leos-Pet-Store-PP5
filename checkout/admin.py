from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

# Define inline editing of order line items within the Order admin page
class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)

    # show these fields but don’t let me edit them
    readonly_fields = (
        'order_number', 'date',
        'delivery_cost', 'order_total', 'grand_total',
        'original_bag', 'stripe_pid'
    )

    fields = (
    'order_number', 'user_profile', 'date', 'full_name',
    'email', 'phone_number', 'country',
    'postcode', 'town_or_city', 'street_address',
    'county', 'delivery_cost',
    'order_total', 'grand_total', 'original_bag',
    'stripe_pid',
    )

    # Columns to display in the order list view
    list_display = (
        'order_number', 'date', 'full_name',
        'order_total', 'delivery_cost', 'grand_total',
        'original_bag', 'stripe_pid'
    )

    # Order the list so newest orders appear first
    ordering = ('-date',)