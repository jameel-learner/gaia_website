from django.shortcuts import render

# Create your views here.
# ##########################################################################
# 
# ERP Feature: Supply Chain Mgmt
# 	Purchase Enquiry Request 		| PRs
# 	Compare Quotations
# 	Confirm Purchase Orders 		| POs
# 	PurchaseInvoicePDFs -- PurchaseOrder
# 	PurchaseOrder Status Tracking -- 
# 		PurchaseOrder -- | Enquiry | Quotation | Confirmed | Dispatched | Received | Paid | 
#
# 	PurchaseOrder Payment Transfer  | payment:purchase_order_payment_transfer
# 
# ##########################################################################


def purchase_enquiry_request(request):
    print("reached purchase_enquiry_request")
    return render(request,'purchase_enquiry_request.html')

def purchase_compare_quote(request):
    print("reached purchase_compare_quote")
    return render(request,'purchase_compare_quote.html')

def confirm_purchase_order(request):
    print("reached confirm_purchase_order")
    return render(request,'confirm_purchase_order.html')

def purchase_order_invoice_pdf(request):
    print("reached purchase_order_invoice_pdf")
    return render(request,'purchase_order_invoice_pdf.html')

def purchase_order_tracking(request):
    print("reached purchase_order_tracking")
    return render(request,'purchase_order_tracking.html')

# def purchase_order_payment_transfer(request):
#     print("reached purchase_order_payment_transfer")
#     return render(request,'purchase_order_payment_transfer.html')
