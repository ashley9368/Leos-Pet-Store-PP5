from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for reaching out! We’ll get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'There was a problem. Please check the form.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})