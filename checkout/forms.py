from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county_or_state','postcode', 
                  'country',)
        labels = {
            "town_or_city": "Town or City",
            "county_or_state": "County/State",
            "phone_number": "Phone Number",
            "street_address1": "Street Address",
            "street_address2": "Continued - if required",
        }