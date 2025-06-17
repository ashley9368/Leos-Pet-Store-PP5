from django.contrib import admin
from .models import Product, Category, ProductVote

class ProductAdmin(admin.ModelAdmin):
    # Show these columns in the Products page
    list_display = (
        'name',
        'category',
        'price',
        'upvotes',
        'downvotes',
        'is_flagged',
        'is_visible',
    )
    readonly_fields = ('upvotes', 'downvotes', 'is_flagged')

# Models for the admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductVote)