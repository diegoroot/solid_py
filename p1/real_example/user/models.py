from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    code = models.CharField(max_length=20, db_column='ID', primary_key=True)
    name = models.CharField(max_length=20, db_column='NAME')
    state = models.CharField(max_length=1, db_column='STATE')
    created_date = models.DateTimeField(db_column='FECHA_CREA', editable=False, null=False)
    updated_date = models.DateTimeField(db_column='FECHA_MODIFICA', editable=False, null=True)

    class Meta:
        db_table = 'USER'
        verbose_name = "USERS"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_date:
            self.created_date = datetime.datetime.today()
        self.updated_date = datetime.datetime.today()
        return super(User, self).save(*args, **kwargs)
