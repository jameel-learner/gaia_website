import json

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as website_login, logout as website_logout
from django.contrib import messages
# Create your views here.
# #########################################################################
# User
#     Registration                          | Verification, Activation
#     Login
#     Logout
#     Forgot
#
#     Product Rating                        | Rating Notification, Post SOs Completion
#     Customer Service Reviews              | Review Notification, Post SOs Completion
# #########################################################################
# from accounts.backends import AuthBackend
# from cpanel.models import VendorDetail, CustomerDetail
# from helper.models import NatureCode
from helper.views import load_request_data, validate_to_trust_uploads
# from accounts.models import User


def register(request):
    print("reached register")
    if request.POST:
        upload_form_fields = [
            'form_of', 'username', 'password', 'captcha', 'customer_id', 'vendor_id', 'type_function',
            'name', 'address', 'contact_number', 'code_word', 'nature_code', 'rating', 'years_of_exp', ]
        upload_file_fields = ['photo', 'doc', ]
        form_data = {}
        load_request_data(form_data, upload_form_fields, request, 'FORM')
        load_request_data(form_data, upload_file_fields, request, 'FILE')
        print(form_data)
        #
        # if form_data['form_of'] == 'login':
        #     try:
        #         auth_obj = AuthBackend()
        #         print(f'auth - username: {form_data["username"]} password: {form_data["password"]}')
        #         user_obj = auth_obj.authenticate(username=form_data['username'], password=form_data['password'])
        #     except:
        #         user_obj = None
        #     print(f'user found : {user_obj}')
        #     if user_obj is not None:
        #         website_login(request, user_obj, backend='accounts.backends.AuthBackend')
        #         if not user_obj.is_superuser:
        #             return redirect('website:search')
        #         return redirect('../../cpanel/index')
        #
        # elif form_data['form_of'] == 'is_username_exists':
        #     context = {"is_username_exists": User.objects.filter(username=form_data['username']).exists()}
        #     return HttpResponse(json.dumps(context))
        #
        # elif form_data['form_of'] == 'vendor':
        #     user_ved_obj = VendorDetail.objects.get(id=form_data['vendor_id'])
        #     if form_data['type_function'] == 'new':
        #         if User.objects.filter(username=form_data['username']).exists:
        #             messages.warning(request, f"Failed !!! <br>User named {form_data['username']} already exists !")
        #             return redirect(f'../../cpanel/index?coming_from={form_data["form_of"]}')
        #         user_obj = User.objects.create(username=form_data['username'], password=make_password(form_data['password']))
        #         user_ved_obj.user = user_obj
        #     # else:
        #     #     user_obj = User.objects.filter(username=form_data['username'])[0]
        #     user_ved_obj.code_word = form_data['code_word']
        #     user_ved_obj.nature_code = NatureCode.objects.get(code=form_data['nature_code'])
        #     user_ved_obj.save()
        #     # user_ved_obj = VendorDetail.objects.create(
        #     #     user=user_obj, name=form_data['name'], code_word=form_data['code_word'],
        #     #     nature_code=NatureCode.objects.filter(code=form_data['nature_code'])[0])
        #     # if form_data['photo']:
        #     #     trust_doc = validate_to_trust_uploads(form_data['photo'], request)
        #     #     if trust_doc:
        #     #         user_ved_obj.photo = trust_doc
        #     # if form_data['doc']:
        #     #     trust_doc = validate_to_trust_uploads(form_data['doc'], request)
        #     #     if trust_doc:
        #     #         user_ved_obj.doc = trust_doc
        #     # user_ved_obj.save()
        #     messages.success(request, f"Vendor User for {user_ved_obj.name} Created Successfully! "
        #                               f"<br>Kindly note the Vendor Code <b style='color:red'>{user_ved_obj.code_word}</b>")
        #
        # elif form_data['form_of'] == 'customer':
        #     user_ved_obj = CustomerDetail.objects.get(id=form_data['customer_id'])
        #     if form_data['type_function'] == 'new':
        #         if User.objects.filter(username=form_data['username']).exists():
        #             messages.warning(request, f"Failed !!! <br>User named {form_data['username']} already exists !")
        #             return redirect(f'../../cpanel/index?coming_from={form_data["form_of"]}')
        #         user_obj = User.objects.create(username=form_data['username'], password=make_password(form_data['password']))
        #         user_ved_obj.user = user_obj
        #     # else:
        #     #     user_obj = User.objects.filter(username=form_data['username'])[0]
        #     user_ved_obj.code_word = form_data['code_word']
        #     user_ved_obj.nature_code = NatureCode.objects.get(code=form_data['nature_code'])
        #     user_ved_obj.save()
        #     # user_ved_obj = CustomerDetail.objects.create(
        #     #     user=user_obj, name=form_data['name'], code_word=form_data['code_word'], nature_code=NatureCode.objects.get(code=form_data['nature_code']))
        #     # if form_data['photo']:
        #     #     trust_doc = validate_to_trust_uploads(form_data['photo'], request)
        #     #     if trust_doc:
        #     #         user_ved_obj.photo = trust_doc
        #     # if form_data['doc']:
        #     #     trust_doc = validate_to_trust_uploads(form_data['doc'], request)
        #     #     if trust_doc:
        #     #         user_ved_obj.doc = trust_doc
        #     # user_ved_obj.save()
        #     messages.success(request, f"Customer User for {user_ved_obj.name} Created Successfully!"
        #                               f"<br>Kindly note the Customer Code <b style='color:red'>{user_ved_obj.code_word}</b>")

    return redirect(f'../../cpanel/index?coming_from={form_data["form_of"]}')
    # return render(request,'login.html')


def login(request):
    print("reached login")
    context = {
        # 'nature_code': NatureCode.objects.all()
    }
    return render(request,'login.html', context)


def logout(request):
    print("reached logout")
    website_logout(request)
    request.session.flush()
    return redirect('../../cpanel/index')
    # return render(request,'logout.html')


def forgot(request):
    print("reached forgot")
    return render(request,'forgot.html')

def product_rating(request):
    print("reached product_rating")
    return render(request,'product_rating.html')

def customer_service_review(request):
    print("reached customer_service_review")
    return render(request,'customer_service_review.html')


# #########################################################################
# Cart
# 	View Cart 								| Remove
# 	Checkout
# 	Get Quote								| Quotation Append to Cart Item
# 	Raise Logistics Service Request 		| logistic:service_enquiry_request
#
# 	View Wishlist 							| Remove
# 	Wishlist Add to Cart					| Wishlist Notification
#
# 	CheckOut - CustomerSalesOrder			| sales:customer_sales_order
# 	CustomerSalesOrder Status Tracking 		| sales:sales_order_tracking
# #########################################################################


def view_cart(request):
    print("reached view_cart")
    return render(request,'view_cart.html')

def product_quote(request):
    print("reached product_quote")
    return render(request,'product_quote.html')

def checkout(request):
    print("reached checkout")
    return render(request,'checkout.html')

# def sales_order(request):
#     print("reached sales_order")
#     return render(request,'confirm_sales_order.html')
#
# def sales_order_tracking(request):
#     print("reached sales_order_tracking")
#     return render(request,'sales_order_tracking.html')

def view_wishlist(request):
    print("reached view_wishlist")
    return render(request,'view_wishlist.html')

def wishlist_add_to_cart(request):
    print("reached wishlist_add_to_cart")
    return render(request,'wishlist_add_to_cart.html')
