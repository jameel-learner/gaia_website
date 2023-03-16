import json
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from cpanel.models import *
from helper.models import *


def load_request_data(data, fields, request, data_type):
    for field in fields:
        if data_type == 'FORM':
            data[field] = request.POST.get(field)
            if not data[field]:
                data[field] = request.GET.get(field)
        elif data_type == 'FILE':
            data[field] = request.FILES.get(field)


def validate_to_trust_uploads(uploaded_file, request):
    allowed_types = {"image/jpeg", "image/jpg", "image/gif", "image/png"}
    print(f"uploaded_file : {uploaded_file}")
    if uploaded_file.size > 1024*1024*2:
        messages.success(request, "Kindly select only Image file (< 2MB in size)")
        print(f"File size more than Max Allowed size: {uploaded_file.size}")
        return None
    elif uploaded_file.content_type not in allowed_types:
        messages.success(request, "Kindly select only Image file (jpeg, png, gif)")
        print(f"Not a valid file type : {uploaded_file.content_type}")
        return None

    print(f"trust-doc : {uploaded_file}")
    return uploaded_file


def object_of(value, nature_string, data_type):
    value = value.strip(' ')
    nature = None
    # if nature_string:
    #     if NatureCode.objects.filter(name=nature_string).exists():
    #         nature = NatureCode.objects.filter(name=nature_string)[0]
    #     else:
    #         code = NATURE_CODES[nature_string] if nature_string in NATURE_CODES else nature_string[0:3].upper()
    #         if NatureCode.objects.filter(code=code).exists():
    #             nature = NatureCode.objects.filter(code=code)[0]
    #         else:
    #             nature = NatureCode.objects.create(name=nature_string, code=code)
    # else:
    #     if NatureCode.objects.filter(name='Un Categorized').exists():
    #         nature = NatureCode.objects.filter(name='Un Categorized')[0]
    #     else:
    #         nature = NatureCode.objects.create(name='Un Categorized', code='UNCAT')
    #
    # if data_type == 'VendorDetail':
    #     if VendorDetail.objects.filter(name=value).exists():
    #         # print(f'VendorDetail: {VendorDetail.objects.filter(name=value)[0]}')
    #         return VendorDetail.objects.filter(name=value)[0]
    #     else:
    #         return VendorDetail.objects.create(
    #             name=value, nature_code=nature, code_word=get_code_words(nature.code, 'Vendor'))
    # elif data_type == 'ManufacturerDetail':
    #     if ManufacturerDetail.objects.filter(name=value).exists():
    #         # print(f'ManufacturerDetail: {ManufacturerDetail.objects.filter(name=value)[0]}')
    #         return ManufacturerDetail.objects.filter(name=value)[0]
    #     else:
    #         return ManufacturerDetail.objects.create(
    #             name=value, code_word=get_code_words(value[0:3].upper(), 'Manufacturer'))
    # elif data_type == 'ProductDetail':
    #     if ProductDetail.objects.filter(name=value).exists():
    #         # print(f'ProductDetail: {ProductDetail.objects.filter(name=value)[0]}')
    #         return ProductDetail.objects.filter(name=value)[0]
    #     else:
    #         return ProductDetail.objects.create(name=value)
    #
    # elif data_type == 'CustomerDetail':
    #     if CustomerDetail.objects.filter(name=value).exists():
    #         # print(f'CustomerDetail: {CustomerDetail.objects.filter(name=value)[0]}')
    #         return CustomerDetail.objects.filter(name=value)[0]
    #     else:
    #         return CustomerDetail.objects.create(
    #             name=value, nature_code=nature, code_word=get_code_words(nature.code, 'Customer'))
    #
    # elif data_type == 'CustomerPartNumber':
    #     values = value.split("|")
    #     part_number = values[0]
    #     customer = values[1]
    #     print(f'part_number: {part_number} - customer: {customer}')
    #     if CustomerPartNumber.objects.filter(part_number=part_number).exists():
    #         # print(f'CustomerDetail: {CustomerDetail.objects.filter(name=value)[0]}')
    #         return CustomerPartNumber.objects.filter(part_number=part_number)[0]
    #     else:
    #         return CustomerPartNumber.objects.create(part_number=part_number, customer_id=customer)
    #
    # elif data_type == 'OfYear':
    #     # if OfYear.objects.filter(of_year=value).exists():
    #     #     print(f'OfYear: {OfYear.objects.filter(of_year=value)[0]}')
    #     #     return OfYear.objects.filter(of_year=value)[0]
    #     # else:
    #     #     return OfYear.objects.create(of_year=value)
    #     pass

    # print(f'object_of( {value} , {data_type} ): None')
    return None


def get_captcha(request):
    captcha = get_random_string(length=6, allowed_chars='1234567890CRMSOUCEDITcrmsoucedit')
    iid = get_iid()
    rec = Captcha.objects.create(iid=iid, captcha=captcha)
    context = {"iid":iid, "captcha":captcha}
    return HttpResponse(json.dumps(context))


def get_code_words(nature_code, code_for):
    unique_code_word = f'{nature_code}{datetime.now().strftime("%f")}'
    print(f'F - {unique_code_word}')
    # if code_for == 'Vendor':
    #     while VendorDetail.objects.filter(code_word=unique_code_word).exists():
    #         unique_code_word = f'{nature_code}{datetime.now().strftime("%f")}'
    #         print(f'V - {unique_code_word}')
    # elif code_for == 'Customer':
    #     while CustomerDetail.objects.filter(code_word=unique_code_word).exists():
    #         unique_code_word = f'{nature_code}{datetime.now().strftime("%f")}'
    #         print(f'C - {unique_code_word}')
    # elif code_for == 'Manufacturer':
    #     while ManufacturerDetail.objects.filter(code_word=unique_code_word).exists():
    #         unique_code_word = f'{nature_code}{datetime.now().strftime("%f")}'
    #         print(f'M - {unique_code_word}')
    # elif code_for == 'CustomerRFQ':
    #     unique_code_word = f'{nature_code}{datetime.now().strftime("%Y-%f")}'
    #     print(f'R - {unique_code_word}')
    #     while CustomerRFQ.objects.filter(rfq_number=unique_code_word).exists():
    #         unique_code_word = f'{nature_code}{datetime.now().strftime("%Y-%f")}'
    #         print(f'R - {unique_code_word}')
    return unique_code_word


def get_code_word(request):
    nature_code = request.POST.get('nature_code')
    code_for = request.POST.get('code_for')
    print(f'{nature_code} -- {code_for}')           # {get_random_string(length=2, allowed_chars="1234567890")}

    unique_code_word = get_code_words(nature_code, code_for)

    context = {"code_word": unique_code_word}
    return HttpResponse(json.dumps(context))


def get_vc_details(request):
    # vc_id = request.POST.get('vc_id')
    # vc_for = request.POST.get('vc_for')
    # vc_detail = None
    # rfq_number = None
    # print(f'{vc_id} -- {vc_for}')           # {get_random_string(length=2, allowed_chars="1234567890")}
    # if vc_for == 'Vendor':
    #     if VendorDetail.objects.filter(id=vc_id).exists():
    #         vc_detail = VendorDetail.objects.filter(id=vc_id)[0]
    # elif vc_for == 'Customer':
    #     if CustomerDetail.objects.filter(id=vc_id).exists():
    #         vc_detail = CustomerDetail.objects.filter(id=vc_id)[0]
    #     rfq_number = get_code_words('RFQ', 'CustomerRFQ')
    #
    # context = {"status": "Not Found"}
    # if vc_detail and vc_detail.user:
    #     context['status'] = 'Found'
    #     context['username'] = vc_detail.user.username
    #     context['code_word'] = vc_detail.code_word
    #     context['nature_code'] = vc_detail.nature_code.code
    # context['rfq_number'] = rfq_number

    return HttpResponse(json.dumps(context))


def verify_captcha(iid, captcha):
    if Captcha.objects.filter(iid=iid, captcha=captcha).exists():
        Captcha.objects.filter(iid=iid, captcha=captcha).delete()
        return True
    return False


def get_iid():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')


def import_offers(import_data_df):
    # df_records = import_data_df.to_dict("records")
    # model_instances = [ImportOffer(
    #     offer_type=record['OFFER_TYPE'],
    #     nature_code=record['NATURE_CODE'],
    #     vendor=record['VENDOR ID/NAME'],
    #     manufacturer=record['MFR NAME'],
    #     product=record['MFR P/N'],
    #     description=record['DESCRIPTION'],
    #     quantity=convert_to('int', record['QTY'], 0),
    #     cost=convert_to('float', record['COST'], 0.0),
    #     date_code=record['DATE CODE'],
    #     lead_time=record['LEAD TIME'],
    #     spq_moq=record['SPQ/MOQ'],
    #     valid_till=datetime.strptime(f"{record['VALID TILL']}", '%m/%d/%Y').date() if record['VALID TILL'] else datetime.now()+timedelta(days=7),
    #     remark=record['REMARK'],
    #     package=record['PACKAGE'],
    #     ex_works=record['EX-WORKS'],
    # ) for record in df_records]
    # ImportOffer.objects.bulk_create(model_instances)

    return 'Done'


def import_rfqs_pos(import_data_df):
    # df_records = import_data_df.to_dict("records")
    # model_instances = [ImportRFQandPO(
    #     offer_type=record['OFFER_TYPE'],
    #     customer=record['CUSTOMER ID/NAME'],
    #     customer_part_number=record['CUSTOMER P/N'],
    #     rfq_number=record['RFQ NUMBER'],
    #     manufacturer=record['MFR NAME'],
    #     product=record['MFR P/N'],
    #     description=record['DESCRIPTION'],
    #     quantity=convert_to('int', record['QTY'], 0),
    #     target_price=convert_to('float', record['TARGET ($)'], 0.0),
    #     delivery_on=datetime.strptime(f"{record['DELIVERY DATE']}", '%m/%d/%Y').date() if record['DELIVERY DATE'] else datetime.now()+timedelta(days=7),
    #     remark=record['REMARK'],
    # ) for record in df_records]
    # ImportRFQandPO.objects.bulk_create(model_instances)

    return 'Done'


def convert_to(data_type, value, default):
    if data_type == 'float':
        try:
            return float(value)
        except ValueError as ve:
            return default
    elif data_type == 'int':
        try:
            return int(value)
        except ValueError as ve:
            return default
    return default


def fetch_data(request):
    raw_list = []
    # if request.POST:
    #     fetch_from = request.POST.get('from')
    #     like_value = request.POST.get('like')
    #     print(f'fetch_from:{fetch_from} -- like_value:{like_value}')
    #     if fetch_from == 'products':
    #         products = ProductDetail.objects.filter(name__icontains=like_value)
    #         for obj in products:
    #             dict = {'id': obj.id, 'name': obj.name}
    #             raw_list.append(dict)
    #
    #     elif fetch_from == 'manufacturers':
    #         manufacturers = ManufacturerDetail.objects.filter(name__icontains=like_value)
    #         for obj in manufacturers:
    #             dict = {'id': obj.id, 'name': obj.name}
    #             raw_list.append(dict)
    #
    #     elif fetch_from == 'vendors':
    #         vendors = VendorDetail.objects.filter(name__icontains=like_value)
    #         for obj in vendors:
    #             dict = {'id': obj.id, 'name': obj.name}
    #             raw_list.append(dict)
    #
    #     elif fetch_from == 'customers':
    #         customers = CustomerDetail.objects.filter(name__icontains=like_value)
    #         for obj in customers:
    #             dict = {'id': obj.id, 'name': obj.name}
    #             raw_list.append(dict)
    #
    #     elif fetch_from == 'customer_pos':
    #         customer_pos = CustomerPO.objects.filter(Q(po_number__icontains=like_value) | Q(po_status__icontains=like_value))
    #         for obj in customer_pos:
    #             dict = {'id': obj.id, 'name': obj.name}
    #             raw_list.append(dict)

    # print(f'raw_list : {raw_list}')
    return HttpResponse(json.dumps(raw_list))


def fetch_name_of_from(request):
    raw_list = {}
    # if request.POST:
    #     name_of = request.POST.get('name_of')
    #     fetch_from = request.POST.get('fetch_from')
    #     id_value = request.POST.get('id')
    #     if fetch_from == 'spot_offers' and name_of == 'vendor':
    #         try:
    #             obj = SpotOffer.objects.get(id=id_value)
    #             raw_list = {'name': obj.vendor.name}
    #         except Exception as ex:
    #             print(ex)
    #             raw_list = {'name': 'No Name'}
    #
    #     elif fetch_from == 'vendor_leadtime_offers' and name_of == 'vendor':
    #         try:
    #             obj = VendorLeadTimeOffer.objects.get(id=id_value)
    #             raw_list = {'name': obj.vendor.name}
    #         except Exception as ex:
    #             print(ex)
    #             raw_list = {'name': 'No Name'}
    #
    #     elif fetch_from == 'supplier_stock_offers' and name_of == 'vendor':
    #         try:
    #             obj = SupplierStockOffer.objects.get(id=id_value)
    #             raw_list = {'name': obj.vendor.name}
    #         except Exception as ex:
    #             print(ex)
    #             raw_list = {'name': 'No Name'}
    #
    #     elif fetch_from == 'customer_leadtime_offers' and name_of == 'customer':
    #         try:
    #             obj = CustomerLeadTimeOffer.objects.get(id=id_value)
    #             raw_list = {'name': obj.customer.name}
    #         except Exception as ex:
    #             raw_list = {'name': 'No Name'}
    #
    #     elif fetch_from == 'customer_excess_offers' and name_of == 'customer':
    #         try:
    #             obj = CustomerExcessOffer.objects.get(id=id_value)
    #             raw_list = {'name': obj.customer.name}
    #         except Exception as ex:
    #             raw_list = {'name': 'No Name'}
    #
    #     elif fetch_from == 'customer_po_offers' and name_of == 'customer':
    #         try:
    #             obj = CustomerPO.objects.get(id=id_value)
    #             raw_list = {'name': obj.customer.name}
    #         except Exception as ex:
    #             raw_list = {'name': 'No Name'}
    #
    #     elif fetch_from == 'customer_rfq_offers' and name_of == 'customer':
    #         try:
    #             obj = CustomerRFQ.objects.get(id=id_value)
    #             raw_list = {'name': obj.customer.name}
    #         except Exception as ex:
    #             raw_list = {'name': 'No Name'}

    return HttpResponse(json.dumps(raw_list))


def paginate_per_page(queryset, page_number=1, page_size=100):
    print(f'reached paginate_per_page {page_number}')
    page_number = 1 if not page_number else page_number
    page_size = 100 if not page_size else page_size
    print(f'page_number - {page_number}  page_size - {page_size}')
    data_per_page = None
    paginator = Paginator(queryset, page_size)
    try:
        data_per_page = paginator.page(page_number)
    except PageNotAnInteger:
        data_per_page = paginator.page(1)
    except EmptyPage:
        data_per_page = paginator.page(paginator.num_pages)

    return data_per_page


def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
