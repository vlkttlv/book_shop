from django import forms
from shop.models import Order
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name',
                  'last_name',
                  'country',
                  'state',
                  'city',
                  'street',
                  'home',
                  'payment_method']