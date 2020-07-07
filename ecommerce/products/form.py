from django import forms
from .models import OrderItems

class ProductForm(forms.Form):
    prod_id = forms.IntegerField()
    prod_name = forms.CharField(max_length=100)
    prod_price = forms.DecimalField(max_digits=8,decimal_places=2)
    quantity = forms.IntegerField()
    class Meta:
        model=OrderItems
        fields = ['prod_id','prod_name','prod_price','quantity']
