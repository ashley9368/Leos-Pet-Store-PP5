from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a product to the bag, With choice to add product by 1"""
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # if the item is already in the bag, add one more
    if item_id in bag:
        bag[item_id] += 1
    else:
        # first time adding this item, set quantity to 1 and show message
        bag[item_id] = 1
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """Remove an item from the shopping bag"""
    #get bag from session
    bag = request.session.get('bag', {})

    # If the item exists in the bag, delete it
    if item_id in bag:
        product = get_object_or_404(Product, pk=item_id)

        if bag[item_id] > 1:
            bag[item_id] -= 1
            messages.success(request, f"Removed {product.name} from your bag")
        else:
            del bag[item_id]
            messages.success(request, f"Removed {product.name} from your bag")
        # save the updated bag into session
        request.session['bag'] = bag

    return redirect("view_bag")