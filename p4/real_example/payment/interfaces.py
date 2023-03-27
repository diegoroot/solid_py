from .models import Payment

class Loan(Payment):
    
    def intiateLoanSettlement():
        pass

    def intiateRePayment():
        pass

class BankPayment(Payment):

    def intiatePayment():
        print('intiatePayment')
    
    def getTotal(self):
        import ipdb; ipdb.set_trace()
        return self.price * 0.3

class LoanPayment(Loan):

    def intiateLoanSettlement():
        print('intiateLoanSettlement')

    def intiateRePayment():
        print('intiateRePayment')
    
    def status(self):
        print(self.state + ';')
    
    def getPayments():
        return Payment.objects.filter(type='LOAN')
    
    def getTotal(self):
        return self.price * 0.2