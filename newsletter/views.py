from django.shortcuts import render
from django.contrib import messages

def newsletter(request):
    """View to handle email when user submits the newsletter form"""
    if request.method == "POST":
        messages.success(request, "We have received your email.")
    return render(request, "newsletter.html")