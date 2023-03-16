from itertools import chain
from django.shortcuts import render
# from django_pandas.io import read_frame
# import pandas as pd

# Create your views here.
##########################################################################
# Website Features
# ##########################################################################
from cpanel.models import *
# from helper.models import ImportOffer, ImportRFQandPO
from helper.views import load_request_data, paginate_per_page


#
# Home Page (Sub Sections)
# 	Header
# 		Phone | Email | Language | Register | Sign IN
# 		LOGO | Product Search | WishList | Cart
# 		Horizontal Menu Bar
# 			Home | Shop | Categories | Deals | Brands | Contact Us
#
# 	Deals of the Week
# 		Featured
# 		On Sale
# 		Best Rated
#
# 	Popular Categories
#
# 	Best Products Slide Show (Limited count)
#
# 	Hot New Arrivals
# 		Featured
# 		Categories (that have Hot products)
#
# 	Hot Best Sellers
# 		Top 20
# 		Categories (that have Best Sellers)
#
# 	Trends 2020
#
# 	Latest Reviews
#
# 	Recently Viewed
#
# 	Famous Product Brand Logos @ Our Store
#
# 	Subsciption Form
#
# 	Footer
# 		Contact Us (Physical | Phone | Email | Social Media Links)
# 		Quick Links
#
# ##########################################################################
def home(request):
    print("reached home")
    coming_from = request.GET.get('coming_from')
    # offers = ImportOffer.objects.all()[:100]
    # rfqs = ImportRFQandPO.objects.all()[:100]
    context = {
        # 'imported_offers': paginate_per_page(offers, request.GET.get('page'), 100),
        # 'imported_rfqs': paginate_per_page(rfqs, request.GET.get('page'), 100),
        # 'nature_code': NatureCode.objects.all(),
        # 'coming_from': coming_from,
        # 'upload_count': ImportOffer.objects.all().count(),
        # 'upload_rfq_count': ImportRFQandPO.objects.all().count(),
        'on_page': 'dashboard',
    }
    return render(request, 'index.html', context)


def search(request):
    print("reached search")
    # vendors = VendorDetail.objects.all()
    # manufacturers = ManufacturerDetail.objects.all()
    # products = ProductDetail.objects.all()
    # all_customer_pos = CustomerPO.objects.all()
    # customers = CustomerDetail.objects.all()
    # descriptions = VendorDetail.objects.all()

    spot_offers = None
    vendor_leadtime_offers = None
    supplier_stock_offers = None
    customer_excess_offers = None
    customer_leadtime_offers = None
    customer_po_offers = None
    customer_rfq_offers = None
    form_data = {}
    #
    # spot_offers_df = pd.DataFrame()
    # vendor_leadtime_offers_df = pd.DataFrame()
    # supplier_stock_offers_df = pd.DataFrame()
    #
    # customer_excess_offers_df = pd.DataFrame()
    # customer_leadtime_offers_df = pd.DataFrame()
    # customer_po_offers_df = pd.DataFrame()
    # customer_rfq_offers_df = pd.DataFrame()
    #
    # customer_po_items_df = pd.DataFrame()
    # customer_rfq_items_df = pd.DataFrame()

    if request.method == 'POST':
        html_form_fields = [
            'vendor_id', 'manufacturer_id', 'product_id', 'customer_po', 'customer_id', 'description',
            'vendor_like', 'manufacturer_like', 'product_like', 'customer_po_like', 'customer_like',
            'coming_from', 'page',
            'spot_offers_same_page', 'vendor_leadtime_offers_same_page', 'supplier_stock_offers_same_page',
            'customer_excess_offers_same_page', 'customer_leadtime_offers_same_page',
            'customer_po_offers_same_page', 'customer_rfq_offers_same_page'

        ]
        # upload_file_fields = ['id_proof_img_all', 'pass_photo_all']
        load_request_data(form_data, html_form_fields, request, 'FORM')
        # load_request_data(form_data, upload_file_fields, request, 'FILE')
        print(form_data)
    #
    #     if form_data['vendor_id']:
    #         vendor = VendorDetail.objects.get(id=form_data['vendor_id'])
    #         spot_offers_df = spot_offers_df.append(read_frame(vendor.spot_offers.all()))
    #         vendor_leadtime_offers_df = vendor_leadtime_offers_df.append(read_frame(vendor.vendor_lead_time_offers.all()))
    #         supplier_stock_offers_df = supplier_stock_offers_df.append(read_frame(vendor.supplier_stock_offers.all()))
    #         customer_po_items_df = customer_po_items_df.append(read_frame(vendor.customer_po_items.all()))
    #         customer_rfq_items_df = customer_rfq_items_df.append(read_frame(vendor.customer_rfq_items.all()))
    #     # print(f'customer_rfq_items_df vendor_id : {customer_rfq_items_df}')
    #
    #     if form_data['manufacturer_id']:
    #         manufacturer = ManufacturerDetail.objects.get(id=form_data['manufacturer_id'])
    #         spot_offers_df = spot_offers_df.append(read_frame(manufacturer.spot_offers.all()))
    #         vendor_leadtime_offers_df = vendor_leadtime_offers_df.append(read_frame(manufacturer.vendor_lead_time_offers.all()))
    #         supplier_stock_offers_df = supplier_stock_offers_df.append(read_frame(manufacturer.supplier_stock_offers.all()))
    #         customer_excess_offers_df = customer_excess_offers_df.append(read_frame(manufacturer.customer_excess_offers.all()))
    #         customer_leadtime_offers_df = customer_leadtime_offers_df.append(read_frame(manufacturer.customer_lead_time_offers.all()))
    #         customer_po_items_df = customer_po_items_df.append(read_frame(manufacturer.customer_po_items.all()))
    #         customer_rfq_items_df = customer_rfq_items_df.append(read_frame(manufacturer.customer_rfq_items.all()))
    #     # print(f'customer_rfq_items_df manufacturer_id: {customer_rfq_items_df}')
    #
    #     if form_data['product_id']:
    #         product = ProductDetail.objects.get(id=form_data['product_id'])
    #         spot_offers_df = spot_offers_df.append(read_frame(product.spot_offers.all()))
    #         vendor_leadtime_offers_df = vendor_leadtime_offers_df.append(read_frame(product.vendor_lead_time_offers.all()))
    #         supplier_stock_offers_df = supplier_stock_offers_df.append(read_frame(product.supplier_stock_offers.all()))
    #         customer_excess_offers_df = customer_excess_offers_df.append(read_frame(product.customer_excess_offers.all()))
    #         customer_leadtime_offers_df = customer_leadtime_offers_df.append(read_frame(product.customer_lead_time_offers.all()))
    #         customer_po_items_df = customer_po_items_df.append(read_frame(product.customer_po_items.all()))
    #         customer_rfq_items_df = customer_rfq_items_df.append(read_frame(product.customer_rfq_items.all()))
    #     # print(f'customer_rfq_items_df product_id: {customer_rfq_items_df}')
    #
    #     if form_data['customer_id']:
    #         customer = CustomerDetail.objects.get(id=form_data['customer_id'])
    #         customer_excess_offers_df = customer_excess_offers_df.append(read_frame(customer.customer_excess_offers.all()))
    #         customer_leadtime_offers_df = customer_leadtime_offers_df.append(read_frame(customer.customer_lead_time_offers.all()))
    #         customer_po_offers_df = customer_po_offers_df.append(read_frame(customer.customer_pos.all()))
    #         customer_rfq_offers_df = customer_rfq_offers_df.append(read_frame(customer.customer_rfqs.all()))
    #
    #     if form_data['customer_po']:
    #         customer_po = CustomerPO.objects.filter(id=form_data['customer_po'])
    #         customer_po_offers_df = customer_po_offers_df.append(read_frame(customer_po.all()))
    #         # customer = customer_po.customer
    #
    # elif request.user.is_authenticated:
    #     # User is a Vendor
    #     print(f'request.user: {request.user} -- vendor: {request.user.vendor.all()}')
    #     if request.user.vendor.all().exists():
    #         spot_offers_df = spot_offers_df.append(read_frame(SpotOffer.objects.filter(vendor__in=request.user.vendor.all())))
    #         vendor_leadtime_offers_df = vendor_leadtime_offers_df.append(read_frame(VendorLeadTimeOffer.objects.filter(vendor__in=request.user.vendor.all())))
    #         supplier_stock_offers_df = supplier_stock_offers_df.append(read_frame(SupplierStockOffer.objects.filter(vendor__in=request.user.vendor.all())))
    #         # customer_po_items_df = customer_po_items_df.append(read_frame(vendor.customer_po_items.all()))
    #         # customer_rfq_items_df = customer_rfq_items_df.append(read_frame(vendor.customer_rfq_items.all()))
    #
    #     # User is a Manufacturer
    #     if request.user.manufacturer.all().exists():
    #         spot_offers_df = spot_offers_df.append(read_frame(SpotOffer.objects.filter(manufacturer__in=request.user.manufacturer.all())))
    #         vendor_leadtime_offers_df = vendor_leadtime_offers_df.append(read_frame(VendorLeadTimeOffer.objects.filter(manufacturer__in=request.user.manufacturer.all())))
    #         supplier_stock_offers_df = supplier_stock_offers_df.append(read_frame(SupplierStockOffer.objects.filter(manufacturer__in=request.user.manufacturer.all())))
    #         customer_excess_offers_df = customer_excess_offers_df.append(read_frame(CustomerExcessOffer.objects.filter(manufacturer__in=request.user.manufacturer.all())))
    #         customer_leadtime_offers_df = customer_leadtime_offers_df.append(read_frame(CustomerLeadTimeOffer.objects.filter(manufacturer__in=request.user.manufacturer.all())))
    #         # customer_po_items_df = customer_po_items_df.append(read_frame(manufacturer.customer_po_items.all()))
    #         # customer_rfq_items_df = customer_rfq_items_df.append(read_frame(manufacturer.customer_rfq_items.all()))
    #
    #     # User is a Customer
    #     if request.user.customer.all().exists():
    #         customer_excess_offers_df = customer_excess_offers_df.append(read_frame(CustomerExcessOffer.objects.filter(customer__in=request.user.customer.all())))
    #         customer_leadtime_offers_df = customer_leadtime_offers_df.append(read_frame(CustomerLeadTimeOffer.objects.filter(customer__in=request.user.customer.all())))
    #         customer_po_offers_df = customer_po_offers_df.append(read_frame(CustomerPO.objects.filter(customer__in=request.user.customer.all())))
    #         customer_rfq_offers_df = customer_rfq_offers_df.append(read_frame(CustomerRFQ.objects.filter(customer__in=request.user.customer.all())))
    #
    # # print(f'spot_offers_df: {spot_offers_df}')
    # spot_offers_df.drop_duplicates(subset="id", keep='first', inplace=True)
    # spot_offers = spot_offers_df.to_dict("records")
    # vendor_leadtime_offers_df.drop_duplicates(subset="id", keep='first', inplace=True)
    # vendor_leadtime_offers = vendor_leadtime_offers_df.to_dict("records")
    # supplier_stock_offers_df.drop_duplicates(subset="id", keep='first', inplace=True)
    # supplier_stock_offers = supplier_stock_offers_df.to_dict("records")
    #
    # customer_excess_offers_df.drop_duplicates(subset="id", keep='first', inplace=True)
    # customer_excess_offers = customer_excess_offers_df.to_dict("records")
    # customer_leadtime_offers_df.drop_duplicates(subset="id", keep='first', inplace=True)
    # customer_leadtime_offers = customer_leadtime_offers_df.to_dict("records")
    # customer_rfq_offers_df.drop_duplicates(subset="id", keep='first', inplace=True)
    # customer_rfq_offers = customer_rfq_offers_df.to_dict("records")
    #
    # # print(f'customer_po_items_df : {customer_po_items_df}')
    # customer_po_items_df.drop_duplicates(subset="customer_po", keep='first', inplace=True)
    # customer_po_items = customer_po_items_df.to_dict("records")
    # for po in customer_po_items:
    #     customer_po_offers_df = customer_po_offers_df.append(
    #         read_frame(CustomerPO.objects.filter(id=po['customer_po'])))
    # customer_po_offers_df.drop_duplicates(subset="id", keep='first', inplace=True)
    # customer_po_offers = customer_po_offers_df.to_dict("records")
    #
    # # print(f'customer_rfq_items_df : {customer_rfq_items_df}')
    # customer_rfq_items_df.drop_duplicates(subset="customer_rfq", keep='first', inplace=True)
    # customer_rfq_items = customer_rfq_items_df.to_dict("records")
    # # print(f'customer_rfq_items dict : {customer_rfq_items}')
    # for rfq in customer_rfq_items:
    #     customer_rfq_offers_df = customer_rfq_offers_df.append(
    #         read_frame(CustomerRFQ.objects.filter(id=rfq['customer_rfq'])))
    # # print(f'customer_rfq_offers cust RFQs dict : {customer_rfq_offers}')
    # customer_rfq_offers_df.drop_duplicates(subset="id", keep='first', inplace=True)
    # customer_rfq_offers = customer_rfq_offers_df.to_dict("records")

    context = {
        # 'vendors' : vendors,
        # 'manufacturers': manufacturers,
        # 'products': products,
        # 'customer_pos': all_customer_pos,
        # 'customers': customers,
        # 'descriptions': descriptions,
        'spot_offers': paginate_per_page(
            spot_offers, request.GET.get('page') if form_data['coming_from'] == 'spot_offers' else form_data['spot_offers_same_page'], 100),
        'vendor_leadtime_offers': paginate_per_page(
            vendor_leadtime_offers, request.GET.get('page') if form_data['coming_from'] == 'vendor_leadtime_offers' else form_data['vendor_leadtime_offers_same_page'], 100),
        'customer_excess_offers': paginate_per_page(
            customer_excess_offers, request.GET.get('page') if form_data['coming_from'] == 'customer_excess_offers' else form_data['customer_excess_offers_same_page'], 100),
        'customer_leadtime_offers': paginate_per_page(
            customer_leadtime_offers, request.GET.get('page') if form_data['coming_from'] == 'customer_leadtime_offers' else form_data['customer_leadtime_offers_same_page'], 100),
        'supplier_stock_offers': paginate_per_page(
            supplier_stock_offers, request.GET.get('page') if form_data['coming_from'] == 'supplier_stock_offers' else form_data['supplier_stock_offers_same_page'], 100),
        'customer_po_offers': paginate_per_page(
            customer_po_offers, request.GET.get('page') if form_data['coming_from'] == 'customer_po_offers' else form_data['customer_po_offers_same_page'], 100),
        'customer_rfq_offers': paginate_per_page(
            customer_rfq_offers, request.GET.get('page') if form_data['coming_from'] == 'customer_rfq_offers' else form_data['customer_rfq_offers_same_page'], 100),
        'form_data': form_data,
        'count_of': {
            'spot_offers': len(spot_offers) if spot_offers else 0,
            'vendor_leadtime_offers': len(vendor_leadtime_offers) if vendor_leadtime_offers else 0,
            'customer_excess_offers': len(customer_excess_offers) if customer_excess_offers else 0,
            'customer_leadtime_offers': len(customer_leadtime_offers) if customer_leadtime_offers else 0,
            'supplier_stock_offers': len(supplier_stock_offers) if supplier_stock_offers else 0,
            'customer_po_offers': len(customer_po_offers) if customer_po_offers else 0,
            'customer_rfq_offers': len(customer_rfq_offers) if customer_rfq_offers else 0,
        },
    }
    return render(request,'search_crm.html', context)


def show_rfq_details(request, rfq_id):
    print(f'show_rfq_details of : {rfq_id}')
    rfq_details = None
    # try:
    #     customer_rfq = CustomerRFQ.objects.get(id=rfq_id)
    #     rfq_details = customer_rfq.customer_rfq_items.all()
    # except Exception as ex:
    #     pass
    context = {
        # 'customer_rfq': customer_rfq,
        'rfq_details': rfq_details,
    }
    return render(request,'rfq_details.html', context)

