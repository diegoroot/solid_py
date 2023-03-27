from django.views import View
from django.http import HttpResponse
import json
from .forms import ApiCreateBankPaymentForm, ApiCreateLoanPaymentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .interfaces import BankPayment

# Create your views here.
class CreatePaymentBank(View):
    form_class = ApiCreateBankPaymentForm

    '''
        Función principal, es la encargada la ejecución principal y la que
        reune los pasos
    '''
    @method_decorator(csrf_exempt)
    def post(self, request):
        form = self.form_class(request.POST)
        return self.form_valid(form) if form.is_valid() else self.form_invalid(
            form)

    '''
        Función encargada de responder finalmente
    '''
    @staticmethod
    def response(res):
        return HttpResponse(res, content_type='application/json')

    '''
        Función encargada de crear el pago cuando es válido
    '''
    def form_valid(self, form):
        payment = form.save(commit=False)
        payment.total = payment.getTotal()
        payment.save()

        response_data = json.dumps({
            'success': True,
            'message': 'Pago creado correctamente.'
        })
        return self.response(response_data)

    '''
        Función encargada de responder con los errores que pueda tener
        los parámetros
    '''
    def form_invalid(self, form):
        res = json.dumps({
            'success': False,
            'form_errors': form.errors
        })
        return self.response(res)