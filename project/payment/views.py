from django.shortcuts import render

# Create your views here.
# ##########################################################################
#
# ERP Feature: Payment
# 	SalesOrder Payment Collection			| Advance | Full
# 	Collection Reminders					| Customer
# 	PurchaseOrder Payment Transfer
# 	LogisticsOrder Payment Transfer
# 	Payment Transfer Notifications			| Supplier, Logistics Agent
#
# ##########################################################################


def sales_order_payment_collection(request):
    print("reached sales_order_payment_collection")
    return render(request,'sales_order_payment_collection.html')

def collection_reminder(request):
    print("reached collection_reminder")
    return render(request,'collection_reminder.html')

def purchase_order_payment_transfer(request):
    print("reached purchase_order_payment_transfer")
    return render(request,'purchase_order_payment_transfer.html')

def logistic_order_payment_transfer(request):
    print("reached logistic_order_payment_transfer")
    return render(request,'logistic_order_payment_transfer.html')

def payment_transfer_notification(request):
    print("reached payment_transfer_notification")
    return render(request,'payment_transfer_notification.html')
