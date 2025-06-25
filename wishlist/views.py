from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import WishlistItem
from products.models import Product

# Create your views here.
@login_required
def toggle_wishlist(request, product_id):
    # look for product or show 404
    product = get_object_or_404(Product, id=product_id)

    # See if user has this product in their wishlist
    # If not add it
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    # if it is in their wishlist remove it
    if not created:
        wishlist_item.delete()

    return redirect(request.META.get('HTTP_REFERER',reverse('products')))