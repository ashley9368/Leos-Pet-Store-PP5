from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents
import stripe
import json
from django.views.decorators.http import require_POST

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    public_key = settings.STRIPE_PUBLIC_KEY
    bag = request.session.get('bag', {})

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address': request.POST['street_address'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(pk=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request,
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!"
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request,
                "There was a problem with your form. Please double-check your information."
            )


    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag   = bag_contents(request)
    subtotal      = current_bag['total']
    stripe_amount = round(subtotal * 100)

    # Create the PaymentIntent
    intent = stripe.PaymentIntent.create(
        amount   = stripe_amount,
        currency = settings.STRIPE_CURRENCY,
    )

    # Warn if your key is missing
    if not public_key:
        messages.warning(
            request,
            "Stripe public key is missing. Did you set it in your environment?"
        )

    context = {
        'order_form':        OrderForm(),
        'stripe_public_key': public_key,
        'client_secret':     intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
