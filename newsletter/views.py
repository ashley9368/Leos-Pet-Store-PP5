from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import NewsletterSubscriber

# Create your views here.
def newsletter_signup(request):
    return render(request, 'newsletter.html')

@require_POST
def subscribe(request):
    email = request.POST.get('email')
    if email:
        NewsletterSubscriber.objects.get_or_create(email=email)
    return redirect('newsletter')