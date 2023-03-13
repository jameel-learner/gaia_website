from django.shortcuts import render

# Create your views here.
# ##########################################################################
#
# ERP Feature: Sales Order Mgmt
#   CustomerSalesOrder					| SOs
# 	SalesInvoicePDFs -- CheckoutOrder
# 	SalesOrder Status Tracking --
# 		CustomerSalesOrder -- | Confirmed | Paid | Dispatched | Delivered |
#
# 	SalesOrder Payment Collection       | payment:sales_order_payment_collection
# ##########################################################################


def confirm_sales_order(request):
    print("reached confirm_sales_order")
    return render(request,'confirm_sales_order.html')

def sales_order_invoice_pdf(request):
    print("reached sales_order_invoice_pdf")
    return render(request,'sales_order_invoice_pdf.html')

def sales_order_tracking(request):
    print("reached sales_order_tracking")
    return render(request,'sales_order_tracking.html')
