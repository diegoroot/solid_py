from django import forms
from .models import Sale


class ApiCreateSaleForm(forms.ModelForm):
    client = forms.CharField(required=True)
    taxes = forms.IntegerField(required=True)
    price = forms.IntegerField(required=True)

    class Meta:
        model = Sale
        fields = ('client', 'taxes', 'price')