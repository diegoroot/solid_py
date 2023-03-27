from django import forms
from .models import Payment
from .interfaces import LoanPayment, BankPayment


class ApiCreateLoanPaymentForm(forms.ModelForm):
    code = forms.CharField(required=True)
    client = forms.CharField(required=True)
    state = forms.CharField(required=True)
    price = forms.IntegerField(required=True)
    type = forms.CharField(required=True)

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if Payment.objects.filter(code=code).exists():
            raise forms.ValidationError(
                u'El código de pago ' + str(code) + u' ya existe, por favor ingrese un código diferente')

        return code

    class Meta:
        model = LoanPayment
        fields = ('code', 'client', 'state', 'price', 'type')

class ApiCreateBankPaymentForm(forms.ModelForm):
    code = forms.CharField(required=True)
    client = forms.CharField(required=True)
    state = forms.CharField(required=True)
    price = forms.IntegerField(required=True)
    type = forms.CharField(required=True)

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if Payment.objects.filter(code=code).exists():
            raise forms.ValidationError(
                u'El código de pago ' + str(code) + u' ya existe, por favor ingrese un código diferente')

        return code

    class Meta:
        model = BankPayment
        fields = ('code', 'client', 'state', 'price', 'type')