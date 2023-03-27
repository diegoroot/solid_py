from django.db import models
import datetime

# Create your models here.
class Bill(models.Model):

    Status = {
        'PENDING': 'PENDING',
        'PAID': 'ON_PROCESS',
        'REFUSED': 'SENT'
    }
    StatusTypes = (
        (Status['PENDING'],  'Pendiente'),
        (Status['PAID'],  'Pagado'),
        (Status['REFUSED'], 'Rechazado'),
    )

    code = models.CharField(max_length=20, db_column='ID', primary_key=True)
    client = models.CharField(max_length=20, db_column='CLIENT_CODE')
    state = models.CharField(max_length=20, db_column='STATE', choices=StatusTypes)
    price = models.IntegerField(db_column='PRICE', null=True)
    created_date = models.DateTimeField(db_column='FECHA_CREA', editable=False, null=False)
    updated_date = models.DateTimeField(db_column='FECHA_MODIFICA', editable=False, null=True)

    class Meta:
        db_table = 'BILL'
        verbose_name = "BILL"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_date:
            self.created_date = datetime.datetime.today()
        self.updated_date = datetime.datetime.today()
        return super(Bill, self).save(*args, **kwargs)
    
    def GenerarFactura(bills):
        bills_resp = []
        for bill in bills:
            bills_resp.append('FACT:' + str(bill.code) + '-' + bill.client + '-' + str(bill.price * 1.16))
        return bills_resp
    
    def export(bill):
        file_name = r'C:\Users\jabg5\OneDrive\Escritorio/' + str(bill.code) + ".txt"
        f= open(file_name,"w+")
        f.write('FACT:' + str(bill.code) + '-' + bill.client + '-' + str(bill.price * 1.16))
        f.close()
