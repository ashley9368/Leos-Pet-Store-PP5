from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from .models import WishlistItem
from products.models import Product


# Create your views here.
@login_required
def toggle_wishlist(request, product_id):
    # look for product or show 404
    product = get_object_or_404(Product, id=product_id)

    # See if user has this product in their wishlist, If not add it
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    # if it is in their wishlist remove it
    if not created:
        wishlist_item.delete()

    return redirect(request.META.get('HTTP_REFERER', reverse('products')))


def wishlist(request):
    """ Show the user their wishlisted items """
    wishlist_items = WishlistItem.objects.filter(
        user=request.user).select_related('product')
    context = {'wishlist_items': wishlist_items, }

    return render(request, 'wishlist.html', context)
