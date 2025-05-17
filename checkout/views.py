from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from .forms import OrderForm
from bag.contexts import bag_contents
import stripe

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    public_key     = settings.STRIPE_PUBLIC_KEY

    # warn if public key is missing
    if not public_key:
        messages.warning(request, "Stripe public key is missing. Did you set it in your env?")

    # get the cart from session
    bag = request.session.get('bag', {})
    if not bag:
        # no items? send back to products
        return redirect(reverse('products'))

    # get the total cost from bag_contents()
    current_bag  = bag_contents(request)
    subtotal     = current_bag['total']

    # Stripe wants amount in pence (so multiply by 100)
    stripe_amount = round(subtotal * 100)

    # ask Stripe for a client secret
    intent = stripe.PaymentIntent.create(
        amount   = stripe_amount,
        currency = settings.STRIPE_CURRENCY,
    )

    print(intent)

    # build the form + Stripe data for the template
    context = {
        'order_form':        OrderForm(),
        'stripe_public_key': public_key,
        'client_secret':     intent.client_secret,
    }

    # show the checkout page
    return render(request, 'checkout/checkout.html', context)
