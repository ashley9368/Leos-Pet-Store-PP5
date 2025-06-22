from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import NewsletterSubscriber
from django.contrib import messages
from django.http import HttpResponse

# Show the newsletter signup page
def newsletter_signup(request):
    #If user subscribed earlier try to get the email from the session
    email = request.session.get('subscribed_email')
    subscriber = None

    if email:
        # If email was found in the session, find the subscriber in the database
        subscriber = NewsletterSubscriber.objects.filter(email=email).first()

    return render(request, 'newsletter.html', {'subscriber': subscriber})

@require_POST
def subscribe(request):
    email = request.POST.get('email')
    if email:
        # Check if the email exists in the database. If not create a new NewsletterSubscriber
        subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)

        if created:
            messages.success(request, "You've been subscribed!")
        else:
            messages.info(request, "You're already subscribed.")

        # Store the email in the session
        request.session['subscribed_email'] = email
    else:
        # If email is empty or missing, show an error message
        messages.error(request, "Please enter a valid email.")

    return redirect('newsletter')

@require_POST
def unsubscribe(request, token):
    try:
        # Try to find the subscriber by their unique unsubscribe token
        subscriber = NewsletterSubscriber.objects.get(unsubscribe_token=token)
        subscriber.delete()
        # Remove the email from the session
        request.session.pop('subscribed_email', None)
        messages.success(request, "You've been unsubscribed.")

    except NewsletterSubscriber.DoesNotExist:
        messages.error(request, "Invalid unsubscribe link.")

    return redirect('newsletter')