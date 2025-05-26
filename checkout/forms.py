from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # Include fields users should fill out
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address', 'town_or_city',
            'postcode', 'country', 'county',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Placeholders for each input
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address': 'Street Address',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False