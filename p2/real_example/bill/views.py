from django.views import View
from django.http import HttpResponse
from .forms import ApiCreateBillForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .interfaces import BillInternational
import json

# Create your views here.
def Home(request):
    return HttpResponse("Hello, World!")


class CreateBill(View):
    form_class = ApiCreateBillForm

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
        Función encargada de crear la factura cuando es válido
    '''
    def form_valid(self, form):
        bill = form.save(commit=False)
        bill.save()
        print(BillInternational.GenerarFactura([bill]))

        response_data = json.dumps({
            'success': True,
            'message': 'Factura creada correctamente.'
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