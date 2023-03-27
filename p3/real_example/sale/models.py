from django.db import models
import datetime

# Create your models here.
class Sale(models.Model):
    client = models.CharField(max_length=20, db_column='CLIENT_CODE')
    price = models.IntegerField(db_column='PRICE', null=True)
    taxes = models.IntegerField(db_column='TAXES', null=True)
    created_date = models.DateTimeField(db_column='FECHA_CREA', editable=False, null=True)
    updated_date = models.DateTimeField(db_column='FECHA_MODIFICA', editable=False, null=True)

    class Meta:
        db_table = 'SALE'
        verbose_name = "SALE"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_date:
            self.created_date = datetime.datetime.today()
        self.updated_date = datetime.datetime.today()
        return super(Sale, self).save(*args, **kwargs)
    
    def generate():
        pass

    def calcule_taxes():
        pass
    