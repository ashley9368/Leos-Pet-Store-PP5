from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """Remove an item from the shopping bag"""
    #get bag from session
    bag = request.session.get('bag', {})

    # If the item exists in the bag, delete it
    if item_id in bag:
        del bag[item_id]
        messages.success(request, "Item removed from your bag")
        #save the updated bag
        request.session['bag'] = bag

    # redirect to the bag page to show updated session
    return redirect('view_bag')