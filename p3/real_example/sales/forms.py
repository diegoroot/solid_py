from django import forms
from .models import SaleAbstract


class ApiCreateSaleForm(forms.ModelForm):
    client = forms.CharField(required=True)
    price = forms.IntegerField(required=True)

    class Meta:
        model = SaleAbstract
        fields = ('client', 'price')