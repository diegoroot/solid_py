from django import forms
from .models import Bill


class ApiCreateBillForm(forms.ModelForm):
    code = forms.CharField(required=True)
    client = forms.CharField(required=True)
    state = forms.CharField(required=True)
    price = forms.IntegerField(required=True)

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if Bill.objects.filter(code=code).exists():
            raise forms.ValidationError(
                u'El código de factura ' + str(code) + u' ya existe, por favor ingrese un código diferente')

        return code

    class Meta:
        model = Bill
        fields = ('code', 'client', 'state', 'price')