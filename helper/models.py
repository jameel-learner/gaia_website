from django.db import models
from datetime import datetime, timedelta


# Create your models here.
OFFER_TYPE = [
    ('Spot Offer', 'Spot Offer'), ('Vendor LeadTime Offer', 'Vendor LeadTime Offer'),
    ('Supplier Stock Offer', 'Supplier Stock  Offer'), ('RFQ', 'RFQ'), ('PO', 'PO'),
    ('Customer LeadTime Offer', 'Customer LeadTime Offer'), ('Customer Excess Offer', 'Customer Excess Offer')]

IMPORT_STATUS_TYPE = [('Loaded', 'Loaded'), ('Valid', 'Valid'), ('Duplicate', 'Duplicate'),
               ('Ignored', 'Ignored'), ('Pushed', 'Pushed'), ('Exists', 'Exists'), ('New Data', 'New Data')]


# Create your models here.
class BaseModel(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Captcha(models.Model):
    iid = models.CharField(max_length=100, blank=False, null=False)
    captcha = models.CharField(max_length=100, blank=False, null=False)
    mainpic = models.ImageField(upload_to='captcha/', blank=True, null=True, default='default300x225.jpg')

    def __str__(self):
        return self.iid


#
# # Vendor, VendorLeadTime, SupplierStock, CustomerLeadTime, CustomerExcess
# class ImportOffer(models.Model):
#     offer_type = models.CharField(choices=OFFER_TYPE, default='Spot Offer', max_length=50)
#     nature_code = models.CharField(max_length=50, blank=True, null=True)
#     vendor = models.CharField(max_length=50, blank=True, null=True)
#     manufacturer = models.CharField(max_length=50, blank=True, null=True)
#     product = models.CharField(max_length=50, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     cost = models.FloatField(blank=True, null=True, default=0.00)
#     date_code = models.CharField(max_length=50, blank=True, null=True)
#     spq_moq = models.CharField(max_length=50, blank=True, null=True)
#     package = models.CharField(max_length=50, blank=True, null=True)
#     ex_works = models.CharField(max_length=50, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     lead_time = models.CharField(max_length=50, blank=True, null=True)
#     valid_till = models.DateField(blank=True, null=True, default=datetime.now()+timedelta(days=7))
#     status = models.CharField(choices=IMPORT_STATUS_TYPE, default='Loaded', max_length=50)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-id']
#
#
# NATURE_CODES = {
#     'OEM': 'OEM',
#     'EMS': 'EMS',
#     'Design house': 'DSG',
#     'System Integrator': 'SIN',
#     'Vendor Customer': 'VNC',
#     'Data Center': 'DAC',
#     'Service / Repair': 'SRC',
#     'Franchise': 'FRN',
#     'Franchise Distributor': 'FRN',
#     'Independent Distributor': 'IND',
#     'Customer Vendor': 'CUV',
# }
#
#
# class NatureCode(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=True)
#     code = models.CharField(max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.code} - {self.name}'
#
#
# class ImportRFQandPO(models.Model):
#     offer_type = models.CharField(choices=OFFER_TYPE, default='RFQ', max_length=50)
#     rfq_number = models.CharField(max_length=50, blank=True, null=True)
#     po_nunber = models.CharField(max_length=50, blank=True, null=True)
#     customer = models.CharField(max_length=50, blank=True, null=True)
#     customer_part_number = models.CharField(max_length=50, blank=True, null=True)
#     manufacturer = models.CharField(max_length=50, blank=True, null=True)
#     product = models.CharField(max_length=50, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     target_price = models.FloatField(blank=True, null=True, default=0.00)
#     delivery_on = models.DateField(blank=True, null=True, default=datetime.now()+timedelta(days=7))
#     remark = models.TextField(blank=True, null=True)
#     status = models.CharField(choices=IMPORT_STATUS_TYPE, default='Loaded', max_length=50)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-id']
#
#
