from django.shortcuts import render

# Create your views here.
# ##########################################################################
#
# ERP Feature: Logistics Mgmt
# 	Service Enquiry Request 		| LRs
# 	Compare Quotations
# 	Confirm Logistics Orders 		| LOs
# 	LogisticsInvoicePDFs -- LogisticsOrder
# 	OrderStatusTracking --
# 		LogisticsOrder -- | Enquiry | Quotation | Confirmed | Picked | Delivered | Paid |
#
# 	LogisticsOrder Payment Transfer | payment:logistic_order_payment_transfer
#
# ##########################################################################


def logistic_enquiry_request(request):
    print("reached logistic_enquiry_request")
    return render(request,'logistic_enquiry_request.html')

def logistic_compare_quote(request):
    print("reached logistic_compare_quote")
    return render(request,'logistic_compare_quote.html')

def confirm_logistic_order(request):
    print("reached confirm_logistic_order")
    return render(request,'confirm_logistic_order.html')

def logistic_order_invoice_pdf(request):
    print("reached logistic_order_invoice_pdf")
    return render(request,'logistic_order_invoice_pdf.html')

def logistic_order_tracking(request):
    print("reached logistic_order_tracking")
    return render(request,'logistic_order_tracking.html')

# def logistic_order_payment_transfer(request):
#     print("reached logistic_order_payment_transfer")
#     return render(request,'logistic_order_payment_transfer.html')
