from django.db import models
import datetime

# Create your models here.
class Payment(models.Model):

    Status = {
        'PENDING': 'PENDING',
        'PAID': 'PAID',
        'REFUSED': 'REFUSED'
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
    type =  models.CharField(max_length=20, db_column='PYMENT_TYPE', null=True)
    created_date = models.DateTimeField(db_column='FECHA_CREA', editable=False, null=False)
    updated_date = models.DateTimeField(db_column='FECHA_MODIFICA', editable=False, null=True)
    total = models.IntegerField(db_column='TOTAL', null=True)

    class Meta:
        db_table = 'PAYMENT'
        verbose_name = "PAYMENT"
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_date:
            self.created_date = datetime.datetime.today()
        self.updated_date = datetime.datetime.today()
        return super(Payment, self).save(*args, **kwargs)
    
    def status(self):
        return self.state
    
    def getPayments():
        return Payment.objects.all()

    def getTotal(self):
        return self.price