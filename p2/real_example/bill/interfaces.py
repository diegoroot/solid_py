from .models import Bill

class BillInternational(Bill):

    def GenerarFactura(bills):
        bills_resp = []
        for bill in bills:
            bills_resp.append('FACT:' + str(bill.code) + '-' + bill.client + '-' + str(bill.price * 1.10))
        return bills_resp

    def export(bills):
        file_name = r'C:\Users\jabg5\OneDrive\Escritorio/' + str(bill.code) + '.csv'
        f= open(file_name,"w+")
        for bill in bills:
            f.write('FACT:' + str(bill.code) + ';' + bill.client + ';' + str(bill.price * 1.16))
        f.close()