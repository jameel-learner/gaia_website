# import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from datetime import datetime, timedelta
# Create your views here.
# ##########################################################################
#
# ERP Features - CPanel
#
#
# ##########################################################################
# from django_pandas.io import read_frame

# from cpanel.models import *
# from helper.models import ImportOffer, ImportRFQandPO
from helper.views import load_request_data      #, import_offers, object_of, import_rfqs_pos, paginate_per_page


def index(request):
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
    return render(request, 'home.html', context)



def load_excel(request):
    form_data = {}
    upload_form_fields = ['rfq_number', 'customer_id', ]
    load_request_data(form_data, upload_form_fields, request, 'FORM')
    upload_file_fields = [
        'spot_offers_excel_file', 'vendor_leadtime_offers_excel_file', 'supplier_stock_offers_excel_file',
        'customer_excess_offers_excel_file', 'customer_leadtime_offers_excel_file',
        'customer_rfq_excel_file', ]
    load_request_data(form_data, upload_file_fields, request, 'FILE')
    print(form_data)
    #
    # if request.method == 'POST' and form_data['spot_offers_excel_file']:
    #     import_data_df = pd.read_excel(form_data['spot_offers_excel_file'])
    #     import_data_df.fillna('', inplace=True)
    #     import_data_df.applymap(lambda x: x.strip(' ') if isinstance(x, str) else x)
    #     # import_data_df.drop_duplicates(subset=['receipt_group', 'income_type', 'of_month', 'of_year'], keep='first', inplace=True)
    #     # print(f"excel data : {import_data_df}")
    #     import_data_df.loc[:, 'OFFER_TYPE'] = 'Spot Offer'
    #     import_offers(import_data_df)
    #
    # if request.method == 'POST' and form_data['vendor_leadtime_offers_excel_file']:
    #     import_data_df = pd.read_excel(form_data['vendor_leadtime_offers_excel_file'])
    #     import_data_df.fillna('', inplace=True)
    #     import_data_df.applymap(lambda x: x.strip(' ') if isinstance(x, str) else x)
    #     # import_data_df.drop_duplicates(subset=['receipt_group', 'income_type', 'of_month', 'of_year'], keep='first', inplace=True)
    #     # print(f"excel data : {import_data_df}")
    #     import_data_df.loc[:, 'OFFER_TYPE'] = 'Vendor LeadTime Offer'
    #     import_offers(import_data_df)
    #
    # if request.method == 'POST' and form_data['supplier_stock_offers_excel_file']:
    #     import_data_df = pd.read_excel(form_data['supplier_stock_offers_excel_file'])
    #     import_data_df.fillna('', inplace=True)
    #     import_data_df.applymap(lambda x: x.strip(' ') if isinstance(x, str) else x)
    #     # import_data_df.drop_duplicates(subset=['receipt_group', 'income_type', 'of_month', 'of_year'], keep='first', inplace=True)
    #     # print(f"excel data : {import_data_df}")
    #     import_data_df.loc[:, 'OFFER_TYPE'] = 'Supplier Stock Offer'
    #     import_offers(import_data_df)
    #
    # if request.method == 'POST' and form_data['customer_leadtime_offers_excel_file']:
    #     import_data_df = pd.read_excel(form_data['customer_leadtime_offers_excel_file'])
    #     import_data_df.fillna('', inplace=True)
    #     import_data_df.applymap(lambda x: x.strip(' ') if isinstance(x, str) else x)
    #     # import_data_df.drop_duplicates(subset=['receipt_group', 'income_type', 'of_month', 'of_year'], keep='first', inplace=True)
    #     # print(f"excel data : {import_data_df}")
    #     import_data_df.loc[:, 'OFFER_TYPE'] = 'Customer LeadTime Offer'
    #     import_offers(import_data_df)
    #
    # if request.method == 'POST' and form_data['customer_excess_offers_excel_file']:
    #     import_data_df = pd.read_excel(form_data['customer_excess_offers_excel_file'])
    #     import_data_df.fillna('', inplace=True)
    #     import_data_df.applymap(lambda x: x.strip(' ') if isinstance(x, str) else x)
    #     # import_data_df.drop_duplicates(subset=['receipt_group', 'income_type', 'of_month', 'of_year'], keep='first', inplace=True)
    #     # print(f"excel data : {import_data_df}")
    #     import_data_df.loc[:, 'OFFER_TYPE'] = 'Customer Excess Offer'
    #     import_offers(import_data_df)
    #
    # if request.method == 'POST' and form_data['customer_rfq_excel_file']:
    #     import_data_df = pd.read_excel(form_data['customer_rfq_excel_file'])
    #     import_data_df.fillna('', inplace=True)
    #     import_data_df.applymap(lambda x: x.strip(' ') if isinstance(x, str) else x)
    #     # import_data_df.drop_duplicates(subset=['receipt_group', 'income_type', 'of_month', 'of_year'], keep='first', inplace=True)
    #     # print(f"excel data : {import_data_df}")
    #     import_data_df.loc[:, 'OFFER_TYPE'] = 'RFQ'     # RFQ or PO
    #     import_data_df.loc[:, 'RFQ NUMBER'] = form_data['rfq_number']     # Actual PROD RFQ ID
    #     import_data_df.loc[:, 'CUSTOMER ID/NAME'] = CustomerDetail.objects.get(id=form_data['customer_id']).name     # Actual PROD Customer Name
    #     import_rfqs_pos(import_data_df)
    #     return redirect('../../cpanel/index?coming_from=load_rfq')

    return redirect('../../cpanel/index?coming_from=load_offer')


def reconcile(request):
    print(f'action_to_perform : {request.POST.get("action_to_perform")}')
    # if request.method == 'POST':
    #     if request.POST.get('action_to_perform') == 'delete_account_data':
    #         ImportOffer.objects.all().delete()
    #         # ExpenseImportData.objects.all().delete()
    #         context = {"message": "Deleted"}
    #         return HttpResponse(json.dumps(context))
    #
    #     elif request.POST.get('action_to_perform') == 'delete_rfq_data':
    #         ImportRFQandPO.objects.all().delete()
    #         # ExpenseImportData.objects.all().delete()
    #         context = {"message": "Deleted"}
    #         return HttpResponse(json.dumps(context))
    #
    #     elif request.POST.get('action_to_perform') == 'validate_on_prod':
    #         if request.POST.get('coming_from') == 'load_offer':
    #             ImportOffer.objects.filter(status='Loaded').update(status='New Data')
    #         elif request.POST.get('coming_from') == 'load_rfq':
    #             ImportRFQandPO.objects.filter(status='Loaded').update(status='New Data')
    #
    #         context = {"message": "Validated"}
    #         return HttpResponse(json.dumps(context))
    #
    #     elif request.POST.get('action_to_perform') == 'push_to_prod':
    #         print(f"coming_from: {request.POST.get('coming_from')}")
    #         if request.POST.get('coming_from') == 'load_rfq':
    #             print(f"RFQ : {ImportRFQandPO.objects.filter(offer_type='RFQ', status='New Data').exists()}")
    #             if ImportRFQandPO.objects.filter(offer_type='RFQ', status='New Data').exists():
    #                 df_records = read_frame(ImportRFQandPO.objects.filter(offer_type='RFQ', status='New Data')).to_dict("records")
    #                 new_rfq = ImportRFQandPO.objects.filter(offer_type='RFQ', status='New Data')[0]
    #                 customer = object_of(new_rfq.customer, '', 'CustomerDetail')
    #                 new_rfq_obj = CustomerRFQ.objects.create(
    #                     customer=customer,
    #                     rfq_number=new_rfq.rfq_number,
    #                     remark=new_rfq.remark,
    #                     valid_till=datetime.now()+timedelta(days=7),
    #                 )
    #                 model_instances=[CustomerRFQItems(
    #                     customer_rfq=new_rfq_obj,
    #                     customer_part_number=object_of(
    #                         f"{record['customer_part_number']}|{customer.id}",
    #                         '', 'CustomerPartNumber'),
    #                     manufacturer=object_of(record['manufacturer'], '', 'ManufacturerDetail'),
    #                     product=object_of(record['product'], '', 'ProductDetail'),
    #                     description=record['description'],
    #                     quantity=int(record['quantity']),
    #                     target_price=float(record['target_price']),
    #                     delivery_on=record['delivery_on'],
    #                 ) for record in df_records]
    #                 CustomerRFQItems.objects.bulk_create(model_instances)
    #                 ImportRFQandPO.objects.filter(offer_type='RFQ', status='New Data').update(status='Pushed')
    #
    #         else:
    #             print(f"Spot Offer: {ImportOffer.objects.filter(offer_type='Spot Offer', status='New Data').exists()}")
    #             if ImportOffer.objects.filter(offer_type='Spot Offer', status='New Data').exists():
    #                 df_records = read_frame(ImportOffer.objects.filter(offer_type='Spot Offer', status='New Data')).to_dict("records")
    #                 model_instances = [SpotOffer(
    #                     vendor=object_of(record['vendor'], record['nature_code'], 'VendorDetail'),
    #                     manufacturer=object_of(record['manufacturer'], '', 'ManufacturerDetail'),
    #                     product=object_of(record['product'], '', 'ProductDetail'),
    #                     description=record['description'],
    #                     quantity=int(record['quantity']),
    #                     cost=float(record['cost']),
    #                     date_code=record['date_code'],
    #                     spq_moq=record['spq_moq'],
    #                     package=record['package'],
    #                     ex_works=record['ex_works'],
    #                     remark=record['remark'],
    #                     lead_time=record['lead_time'],
    #                     valid_till=record['valid_till']
    #                 ) for record in df_records]
    #                 SpotOffer.objects.bulk_create(model_instances)
    #                 ImportOffer.objects.filter(status='New Data', offer_type='Spot Offer').update(status='Pushed')
    #
    #             print(f"Vendor LeadTime Offer: {ImportOffer.objects.filter(offer_type='Vendor LeadTime Offer', status='New Data').exists()}")
    #             if ImportOffer.objects.filter(offer_type='Vendor LeadTime Offer', status='New Data').exists():
    #                 df_records = read_frame(ImportOffer.objects.filter(offer_type='Vendor LeadTime Offer', status='New Data')).to_dict("records")
    #                 model_instances = [VendorLeadTimeOffer(
    #                     vendor=object_of(record['vendor'], record['nature_code'], 'VendorDetail'),
    #                     manufacturer=object_of(record['manufacturer'], '', 'ManufacturerDetail'),
    #                     product=object_of(record['product'], '', 'ProductDetail'),
    #                     description=record['description'],
    #                     quantity=int(record['quantity']),
    #                     cost=float(record['cost']),
    #                     date_code=record['date_code'],
    #                     spq_moq=record['spq_moq'],
    #                     package=record['package'],
    #                     ex_works=record['ex_works'],
    #                     remark=record['remark'],
    #                     lead_time=record['lead_time'],
    #                     valid_till=record['valid_till']
    #                 ) for record in df_records]
    #                 VendorLeadTimeOffer.objects.bulk_create(model_instances)
    #                 ImportOffer.objects.filter(status='New Data', offer_type='Vendor LeadTime Offer').update(status='Pushed')
    #
    #             print(f"Supplier Stock Offer: {ImportOffer.objects.filter(offer_type='Supplier Stock Offer', status='New Data').exists()}")
    #             if ImportOffer.objects.filter(offer_type='Supplier Stock Offer', status='New Data').exists():
    #                 df_records = read_frame(ImportOffer.objects.filter(offer_type='Supplier Stock Offer', status='New Data')).to_dict("records")
    #                 model_instances = [SupplierStockOffer(
    #                     vendor=object_of(record['vendor'], record['nature_code'], 'VendorDetail'),
    #                     manufacturer=object_of(record['manufacturer'], '', 'ManufacturerDetail'),
    #                     product=object_of(record['product'], '', 'ProductDetail'),
    #                     description=record['description'],
    #                     quantity=int(record['quantity']),
    #                     cost=float(record['cost']),
    #                     date_code=record['date_code'],
    #                     spq_moq=record['spq_moq'],
    #                     package=record['package'],
    #                     ex_works=record['ex_works'],
    #                     remark=record['remark'],
    #                     lead_time=record['lead_time'],
    #                     valid_till=record['valid_till']
    #                 ) for record in df_records]
    #                 SupplierStockOffer.objects.bulk_create(model_instances)
    #                 ImportOffer.objects.filter(status='New Data', offer_type='Supplier Stock Offer').update(status='Pushed')
    #
    #             print(f"Customer LeadTime Offer: {ImportOffer.objects.filter(offer_type='Customer LeadTime Offer', status='New Data').exists()}")
    #             if ImportOffer.objects.filter(offer_type='Customer LeadTime Offer', status='New Data').exists():
    #                 df_records = read_frame(ImportOffer.objects.filter(offer_type='Customer LeadTime Offer', status='New Data')).to_dict("records")
    #                 model_instances = [CustomerLeadTimeOffer(
    #                     customer=object_of(record['vendor'], record['nature_code'], 'CustomerDetail'),
    #                     manufacturer=object_of(record['manufacturer'], '', 'ManufacturerDetail'),
    #                     product=object_of(record['product'], '', 'ProductDetail'),
    #                     description=record['description'],
    #                     quantity=int(record['quantity']),
    #                     cost=float(record['cost']),
    #                     date_code=record['date_code'],
    #                     spq_moq=record['spq_moq'],
    #                     package=record['package'],
    #                     ex_works=record['ex_works'],
    #                     remark=record['remark'],
    #                     lead_time=record['lead_time'],
    #                     valid_till=record['valid_till']
    #                 ) for record in df_records]
    #                 CustomerLeadTimeOffer.objects.bulk_create(model_instances)
    #                 ImportOffer.objects.filter(status='New Data', offer_type='Customer LeadTime Offer').update(status='Pushed')
    #
    #             print(f"Customer Excess Offer: {ImportOffer.objects.filter(offer_type='Customer Excess Offer', status='New Data').exists()}")
    #             if ImportOffer.objects.filter(offer_type='Customer Excess Offer', status='New Data').exists():
    #                 df_records = read_frame(ImportOffer.objects.filter(offer_type='Customer Excess Offer', status='New Data')).to_dict("records")
    #                 model_instances = [CustomerExcessOffer(
    #                     customer=object_of(record['vendor'], record['nature_code'], 'CustomerDetail'),
    #                     manufacturer=object_of(record['manufacturer'], '', 'ManufacturerDetail'),
    #                     product=object_of(record['product'], '', 'ProductDetail'),
    #                     description=record['description'],
    #                     quantity=int(record['quantity']),
    #                     cost=float(record['cost']),
    #                     date_code=record['date_code'],
    #                     spq_moq=record['spq_moq'],
    #                     package=record['package'],
    #                     ex_works=record['ex_works'],
    #                     remark=record['remark'],
    #                     lead_time=record['lead_time'],
    #                     valid_till=record['valid_till']
    #                 ) for record in df_records]
    #                 CustomerExcessOffer.objects.bulk_create(model_instances)
    #                 ImportOffer.objects.filter(status='New Data', offer_type='Customer Excess Offer').update(status='Pushed')
    #
    #         context = {"message": "Pushed to PROD"}
    #         return HttpResponse(json.dumps(context))

    return redirect('../../cpanel/index')


