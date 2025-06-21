from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

#Fixed delivery fee
FIXED_DELIVERY_FEE = Decimal('5.00') 

def bag_contents(request):

    bag_items = []
    total = 0 
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': product.price * quantity,
        })
     
    #Add delivery fee if bag isn't empty
    delivery = FIXED_DELIVERY_FEE if product_count > 0 else 0
    # Add final total including delivery
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context