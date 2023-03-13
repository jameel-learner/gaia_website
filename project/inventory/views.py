from django.shortcuts import render

# Create your views here.
# ##########################################################################
#
# ERP Feature: Inventory Mgmt
# 	Product Stock Check
# 	Product Stock Update			| Post - Sales | Purchase
# 	Product Costing 				| Landing Price,
# 	Product Pricing Profit Margin	| MRPs
#
# ##########################################################################

def product_stock_check(request):
    print("reached product_stock_check")
    return render(request,'product_stock_check.html')

def product_stock_update(request):
    print("reached product_stock_update")
    return render(request,'product_stock_update.html')

def product_costing(request):
    print("reached product_costing")
    return render(request,'product_costing.html')

def product_pricing(request):
    print("reached product_pricing")
    return render(request,'product_pricing.html')
