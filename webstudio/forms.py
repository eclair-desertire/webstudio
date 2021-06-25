from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    
    class Meta:
        model=Order
        
        fields=('order_title','order_info','order_date','order_email','order_contacts')
        