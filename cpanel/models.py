from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import User

# Create your models here.
# from helper.models import NatureCode

STATUS_TYPE = [('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Refunded', 'Refunded'), ('Pending', 'Pending'),
               ('Initiated', 'Initiated'), ('Delivered', 'Delivered'), ('Processing', 'Processing'),
               ('InStock', 'InStock'), ('OutOfStock', 'OutOfStock'), ('Quoted', 'Quoted'), ('Completed', 'Completed'),
               ('Approved', 'Approved'), ('Passed', 'Passed'), ('Failed', 'Failed')]

PO_STATUS_TYPE = [('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Closed', 'Closed'), ('Completed', 'Completed')]

QC_STATUS_TYPE = [('Pending', 'Pending'), ('Passed', 'Passed'), ('Failed', 'Failed')]

#
# class VendorDetail(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True, related_name='vendor', on_delete=models.CASCADE)
#     nature_code = models.ForeignKey(NatureCode, blank=True, null=True, related_name='vendor', on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     code_word = models.CharField(max_length=50, blank=True, null=True)
#     location = models.CharField(max_length=50, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     sales_contact_name = models.CharField(max_length=50, blank=True, null=True)
#     sales_contact_email = models.CharField(max_length=50, blank=True, null=True)
#     sales_contact_number = models.CharField(max_length=20, blank=True, null=True)
#     accounts_contact_name = models.CharField(max_length=50, blank=True, null=True)
#     accounts_contact_email = models.CharField(max_length=50, blank=True, null=True)
#     accounts_contact_number = models.CharField(max_length=20, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)            # Annual Revenue, ISO & Other Certification Info
#     rating = models.IntegerField(blank=True, null=True)
#     years_of_exp = models.IntegerField(blank=True, null=True)
#     years_with_us = models.IntegerField(blank=True, null=True)
#     photo = models.ImageField(upload_to='vendor/img', blank=True, null=True)
#     contract_doc = models.FileField(upload_to='vendor/doc', blank=True, null=True)
#     legal_doc = models.FileField(upload_to='vendor/doc', blank=True, null=True)
#     other_doc = models.FileField(upload_to='vendor/doc', blank=True, null=True)
#     is_defense_aerospace = models.BooleanField(default=False)
#     franchised_line_name = models.CharField(max_length=50, blank=True, null=True)
#     non_franchised_line_name = models.CharField(max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return self.code_word if self.code_word else ""
#
#     class Meta:
#         ordering = ['name']
#
#
# class ManufacturerDetail(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True, related_name='manufacturer', on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     contact_number = models.CharField(max_length=20, blank=True, null=True)
#     code_word = models.CharField(max_length=50, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     rating = models.IntegerField(blank=True, null=True)
#     years_of_exp = models.IntegerField(blank=True, null=True)
#     years_with_us = models.IntegerField(blank=True, null=True)
#     photo = models.ImageField(upload_to='manufacture/img', blank=True, null=True)
#     doc = models.FileField(upload_to='manufacture/doc', blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ['name']
#
#
# class CustomerDetail(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True, related_name='customer', on_delete=models.CASCADE)
#     nature_code = models.ForeignKey(NatureCode, blank=True, null=True, related_name='customer', on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     code_word = models.CharField(max_length=50, blank=True, null=True)
#     location = models.CharField(max_length=50, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     industry = models.CharField(max_length=50, blank=True, null=True)
#     segment = models.CharField(max_length=50, blank=True, null=True)
#     trade_ref_company_name = models.CharField(max_length=50, blank=True, null=True)
#     trade_ref_contact_name = models.CharField(max_length=50, blank=True, null=True)
#     trade_ref_contact_email = models.CharField(max_length=50, blank=True, null=True)
#     trade_ref_contact_number = models.CharField(max_length=20, blank=True, null=True)
#     purchase_contact_name = models.CharField(max_length=50, blank=True, null=True)
#     purchase_contact_email = models.CharField(max_length=50, blank=True, null=True)
#     purchase_contact_number = models.CharField(max_length=20, blank=True, null=True)
#     accounts_contact_name = models.CharField(max_length=50, blank=True, null=True)
#     accounts_contact_email = models.CharField(max_length=50, blank=True, null=True)
#     accounts_contact_number = models.CharField(max_length=20, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)      # Annual Revenue, Yearly buying (In USD) for Semiconductor or IT peripherals or Memory
#     rating = models.IntegerField(blank=True, null=True)
#     years_of_exp = models.IntegerField(blank=True, null=True)
#     years_with_us = models.IntegerField(blank=True, null=True)
#     photo = models.ImageField(upload_to='customer/img', blank=True, null=True)
#     contract_doc = models.FileField(upload_to='customer/doc', blank=True, null=True)
#     legal_doc = models.FileField(upload_to='customer/doc', blank=True, null=True)
#     other_doc = models.FileField(upload_to='customer/doc', blank=True, null=True)
#     is_defense_aerospace = models.BooleanField(default=False)
#     is_non_franchised = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.code_word if self.code_word else ""
#
#     class Meta:
#         ordering = ['name']
#
#
# class ProductDetail(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     part_number = models.CharField(max_length=50, blank=True, null=True)
#     code_word = models.CharField(max_length=50, blank=True, null=True)
#     photo = models.ImageField(upload_to='product/img', blank=True, null=True)
#     doc = models.FileField(upload_to='product/doc', blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ['name']
#
#
# class SpotOffer(models.Model):
#     vendor = models.ForeignKey(VendorDetail, null=True, blank=True, related_name='spot_offers',
#                                   on_delete=models.CASCADE)
#     manufacturer = models.ForeignKey(ManufacturerDetail, null=True, blank=True, related_name='spot_offers',
#                                on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetail, null=True, blank=True, related_name='spot_offers',
#                                    on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     cost = models.FloatField(blank=True, null=True, default=0.00)
#     date_code = models.CharField(max_length=50, blank=True, null=True)
#     spq_moq = models.CharField(max_length=50, blank=True, null=True)
#     package = models.CharField(max_length=50, blank=True, null=True)
#     ex_works = models.CharField(max_length=50, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     lead_time = models.CharField(max_length=50, blank=True, null=True)
#     valid_till = models.DateField(blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.product} from {self.vendor}'
#
#     class Meta:
#         ordering = ['-created_on']
#         verbose_name = _("Offer: Spot Offer")
#         verbose_name_plural = _("Offers: Spot Offers")
#
#
# class VendorLeadTimeOffer(models.Model):
#     vendor = models.ForeignKey(VendorDetail, null=True, blank=True, related_name='vendor_lead_time_offers',
#                                   on_delete=models.CASCADE)
#     manufacturer = models.ForeignKey(ManufacturerDetail, null=True, blank=True, related_name='vendor_lead_time_offers',
#                                on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetail, null=True, blank=True, related_name='vendor_lead_time_offers',
#                                    on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     cost = models.FloatField(blank=True, null=True, default=0.00)
#     date_code = models.CharField(max_length=50, blank=True, null=True)
#     spq_moq = models.CharField(max_length=50, blank=True, null=True)
#     package = models.CharField(max_length=50, blank=True, null=True)
#     ex_works = models.CharField(max_length=50, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     lead_time = models.CharField(max_length=50, blank=True, null=True)
#     valid_till = models.DateField(blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.product} from {self.vendor}'
#
#     class Meta:
#         ordering = ['-created_on']
#         verbose_name = _("Offer: Vendor Lead-Time Offer")
#         verbose_name_plural = _("Offers: Vendor Lead-Time Offers")
#
#
# class CustomerExcessOffer(models.Model):
#     customer = models.ForeignKey(CustomerDetail, null=True, blank=True, related_name='customer_excess_offers',
#                                     on_delete=models.CASCADE)
#     manufacturer = models.ForeignKey(ManufacturerDetail, null=True, blank=True, related_name='customer_excess_offers',
#                                on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetail, null=True, blank=True, related_name='customer_excess_offers',
#                                    on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     cost = models.FloatField(blank=True, null=True, default=0.00)
#     date_code = models.CharField(max_length=50, blank=True, null=True)
#     spq_moq = models.CharField(max_length=50, blank=True, null=True)
#     package = models.CharField(max_length=50, blank=True, null=True)
#     ex_works = models.CharField(max_length=50, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     lead_time = models.CharField(max_length=50, blank=True, null=True)
#     valid_till = models.DateField(blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.product} from {self.customer}'
#
#     class Meta:
#         ordering = ['-created_on']
#         verbose_name = _("Offer: Customer Excess Offer")
#         verbose_name_plural = _("Offers: Customer Excess Offers")
#
#
# class CustomerLeadTimeOffer(models.Model):
#     customer = models.ForeignKey(CustomerDetail, null=True, blank=True, related_name='customer_lead_time_offers',
#                                     on_delete=models.CASCADE)
#     manufacturer = models.ForeignKey(ManufacturerDetail, null=True, blank=True, related_name='customer_lead_time_offers',
#                                on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetail, null=True, blank=True, related_name='customer_lead_time_offers',
#                                    on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     cost = models.FloatField(blank=True, null=True, default=0.00)
#     date_code = models.CharField(max_length=50, blank=True, null=True)
#     spq_moq = models.CharField(max_length=50, blank=True, null=True)
#     package = models.CharField(max_length=50, blank=True, null=True)
#     ex_works = models.CharField(max_length=50, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     lead_time = models.CharField(max_length=50, blank=True, null=True)
#     valid_till = models.DateField(blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.product} from {self.customer}'
#
#     class Meta:
#         ordering = ['-created_on']
#         verbose_name = _("Offer: Customer  Lead-Time Offer")
#         verbose_name_plural = _("Offers: Customer Lead-Time Offers")
#
#
# class SupplierStockOffer(models.Model):
#     vendor = models.ForeignKey(VendorDetail, null=True, blank=True, related_name='supplier_stock_offers',
#                                   on_delete=models.CASCADE)
#     manufacturer = models.ForeignKey(ManufacturerDetail, null=True, blank=True, related_name='supplier_stock_offers',
#                                on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetail, null=True, blank=True, related_name='supplier_stock_offers',
#                                    on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     cost = models.FloatField(blank=True, null=True, default=0.00)
#     date_code = models.CharField(max_length=50, blank=True, null=True)
#     spq_moq = models.CharField(max_length=50, blank=True, null=True)
#     package = models.CharField(max_length=50, blank=True, null=True)
#     ex_works = models.CharField(max_length=50, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     lead_time = models.CharField(max_length=50, blank=True, null=True)
#     valid_till = models.DateField(blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.product} from {self.vendor}'
#
#     class Meta:
#         ordering = ['-created_on']
#         verbose_name = _("Offer: Supplier Stock Offer")
#         verbose_name_plural = _("Offers: Supplier Stock Offers")
#
#
# class CustomerPO(models.Model):
#     customer = models.ForeignKey(CustomerDetail, null=True, blank=True, related_name='customer_pos',
#                                     on_delete=models.CASCADE)
#     po_number = models.CharField(max_length=50, blank=True, null=True)
#     po_status = models.CharField(choices=PO_STATUS_TYPE, default='Pending', max_length=50)
#     remark = models.TextField(blank=True, null=True)
#     delivery_on = models.DateField(blank=True, null=True)
#     valid_till = models.DateField(blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.id)
#
#     class Meta:
#         ordering = ['-created_on']
#
#
# class CustomerPOItems(models.Model):
#     customer_po = models.ForeignKey(CustomerPO, null=True, blank=True, related_name='customer_po_items',
#                                        on_delete=models.CASCADE)
#     vendor = models.ForeignKey(VendorDetail, null=True, blank=True, related_name='customer_po_items',
#                                   on_delete=models.CASCADE)
#     manufacturer = models.ForeignKey(ManufacturerDetail, null=True, blank=True, related_name='customer_po_items',
#                                on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetail, null=True, blank=True, related_name='customer_po_items',
#                                    on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     qc_status = models.CharField(choices=QC_STATUS_TYPE, default='Pending', max_length=50)
#     qc_status_doc = models.FileField(upload_to='quality/doc', blank=True, null=True)
#     label_doc = models.FileField(upload_to='quality/doc', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.product} from {self.vendor}'
#
#
# class CustomerRFQ(models.Model):
#     customer = models.ForeignKey(CustomerDetail, null=True, blank=True, related_name='customer_rfqs',
#                                     on_delete=models.CASCADE)
#     rfq_number = models.CharField(max_length=50, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     valid_till = models.DateField(blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     rfq_status = models.CharField(choices=STATUS_TYPE, default='Pending', max_length=50)
#
#     def __str__(self):
#         return str(self.id)
#
#     class Meta:
#         ordering = ['-created_on']
#
#
# class CustomerPartNumber(models.Model):
#     customer = models.ForeignKey(CustomerDetail, null=True, blank=True, related_name='customer_part_numbers',
#                                     on_delete=models.CASCADE)
#     part_number = models.CharField(max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return str(self.part_number)
#
#
# class CustomerRFQItems(models.Model):
#     customer_rfq = models.ForeignKey(CustomerRFQ, null=True, blank=True, related_name='customer_rfq_items',
#                                         on_delete=models.CASCADE)
#     customer_part_number = models.ForeignKey(CustomerPartNumber, null=True, blank=True, related_name='customer_rfq_items',
#                                    on_delete=models.CASCADE)
#     vendor = models.ForeignKey(VendorDetail, null=True, blank=True, related_name='customer_rfq_items',
#                                   on_delete=models.CASCADE)
#     manufacturer = models.ForeignKey(ManufacturerDetail, null=True, blank=True, related_name='customer_rfq_items',
#                                on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetail, null=True, blank=True, related_name='customer_rfq_items',
#                                    on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     line_number = models.CharField(max_length=50, blank=True, null=True)
#     target_price = models.FloatField(blank=True, null=True, default=0.00)
#     delivery_on = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.product} from {self.manufacturer}'
#
#
