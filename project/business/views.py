from django.shortcuts import render

# Create your views here.
# ##########################################################################
#
# ERP Feature: Running Expense Mgmt
# 	Against Sales Orders 			| RoundOffs, Loading, P&F
# 	Against Purchase Orders 		| Coli,
# 	Against Logistic Orders 		| Pickup Delays, Tips
# 	Recurring Expenses				| Salaries, Rents,
# 	Fixed Expenses					| Advances, Capital Stock, Customer Credits
#
# ##########################################################################

def sales_order_expenses(request):
    print("reached sales_order_expenses")
    return render(request,'sales_order_expenses.html')

def purchase_order_expenses(request):
    print("reached purchase_order_expenses")
    return render(request,'purchase_order_expenses.html')

def logistic_order_expenses(request):
    print("reached logistic_order_expenses")
    return render(request,'logistic_order_expenses.html')

def recurring_expenses(request):
    print("reached recurring_expenses")
    return render(request,'recurring_expenses.html')

def fixed_expenses(request):
    print("reached fixed_expenses")
    return render(request,'fixed_expenses.html')


# ##########################################################################
#
# ERP Feature: Business Analytics
# 	Optimization 			| Purchase Streamline, Running Expense
# 	Product Performance
# 	Category Performance
#
# ##########################################################################


def optimization(request):
    print("reached optimization")
    return render(request,'optimization.html')

def product_performance(request):
    print("reached product_performance")
    return render(request,'product_performance.html')

def category_performance(request):
    print("reached category_performance")
    return render(request,'category_performance.html')
