from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _
from cpanel.models import *

# Register your models here.

#
# class VendorDetailAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (_('Vendor Details'),
#          {'fields': ('name', 'location', 'address', 'remark', 'rating', 'years_of_exp', 'years_with_us',
#                      'is_defense_aerospace', 'franchised_line_name', 'non_franchised_line_name')}),
#         (_('Sales Contact Details'),
#          {'fields': ('sales_contact_name', 'sales_contact_email', 'sales_contact_number')}),
#         (_('Accounts Contact Details'),
#          {'fields': ('accounts_contact_name', 'accounts_contact_email', 'accounts_contact_number')}),
#         (_('Document Uploads'),
#          {'fields': ('photo', 'contract_doc', 'legal_doc', 'other_doc')}),
#     )
#     list_display = ('name', 'code_word', 'user', 'sales_contact_name', 'accounts_contact_name',)
#     list_filter = ('rating', 'nature_code', 'is_defense_aerospace')
#     search_fields = ('name', 'address', 'sales_contact_name', 'sales_contact_email', 'sales_contact_number',
#                      'accounts_contact_name', 'accounts_contact_email', 'accounts_contact_number', 'remark')
#
#
# class ManufacturerDetailAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code_word', 'contact_number', 'rating', 'years_of_exp')
#     list_filter = ('rating', )
#     search_fields = ('name', 'address', 'contact_number', 'remark')
#
#
# class CustomerDetailAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (_('Customer Details'),
#          {'fields': ('name', 'location', 'address', 'industry', 'segment', 'remark', 'rating', 'years_of_exp', 'years_with_us',
#                      'is_defense_aerospace', 'is_non_franchised')}),
#         (_('Trade Reference Contact Details for Payment Terms'),
#          {'fields': ('trade_ref_company_name', 'trade_ref_contact_name', 'trade_ref_contact_email', 'trade_ref_contact_number')}),
#         (_('Purchase Contact Details'),
#          {'fields': ('purchase_contact_name', 'purchase_contact_email', 'purchase_contact_number')}),
#         (_('Accounts Contact Details'),
#          {'fields': ('accounts_contact_name', 'accounts_contact_email', 'accounts_contact_number')}),
#         (_('Document Uploads'),
#          {'fields': ('photo', 'contract_doc', 'legal_doc', 'other_doc')}),
#     )
#     list_display = ('name', 'code_word', 'user', 'trade_ref_contact_name', 'purchase_contact_name', 'accounts_contact_name',)
#     list_filter = ('rating', 'nature_code', )
#     search_fields = ('name', 'address', 'trade_ref_contact_name', 'purchase_contact_name', 'accounts_contact_name', 'remark')
#
#
# class ProductDetailAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'part_number', 'code_word')
#     # list_filter = ('rating', )
#     search_fields = ('name', 'description', 'part_number', 'code_word')
#
#
# class ProductDetailAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'part_number', 'code_word')
#     # list_filter = ('rating', )
#     search_fields = ('name', 'description', 'part_number', 'code_word')
#
#
# admin.site.register(VendorDetail, VendorDetailAdmin)
# admin.site.register(ManufacturerDetail, ManufacturerDetailAdmin)
# admin.site.register(CustomerDetail, CustomerDetailAdmin)
# admin.site.register(ProductDetail, ProductDetailAdmin)
#
#
# class SpotOfferAdmin(admin.ModelAdmin):
#     list_display = ('created_on', 'vendor', 'manufacturer', 'product', 'description', 'quantity', 'cost', 'date_code',
#                     'lead_time', 'spq_moq', 'package', 'valid_till', 'ex_works', 'remark')
#     list_filter = ('lead_time', 'ex_works', 'valid_till')
#     search_fields = ('vendor__name', 'manufacturer__name', 'product__name', 'description')
#
#
# class VendorLeadTimeOfferAdmin(admin.ModelAdmin):
#     list_display = ('created_on', 'vendor', 'manufacturer', 'product', 'description', 'quantity', 'cost', 'date_code',
#                     'lead_time', 'spq_moq', 'package', 'valid_till', 'ex_works', 'remark')
#     list_filter = ('lead_time', 'ex_works', 'valid_till')
#     search_fields = ('vendor__name', 'manufacturer__name', 'product__name', 'description')
#
#
# class CustomerExcessOfferAdmin(admin.ModelAdmin):
#     list_display = ('created_on', 'customer', 'manufacturer', 'product', 'description', 'quantity', 'cost', 'date_code',
#                     'lead_time', 'spq_moq', 'package', 'valid_till', 'ex_works', 'remark')
#     list_filter = ('lead_time', 'ex_works', 'valid_till')
#     search_fields = ('customer__name', 'manufacturer__name', 'product__name', 'description')
#
#
# class CustomerLeadTimeOfferAdmin(admin.ModelAdmin):
#     list_display = ('created_on', 'customer', 'manufacturer', 'product', 'description', 'quantity', 'cost', 'date_code',
#                     'lead_time', 'spq_moq', 'package', 'valid_till', 'ex_works', 'remark')
#     list_filter = ('lead_time', 'ex_works', 'valid_till')
#     search_fields = ('customer__name', 'manufacturer__name', 'product__name', 'description')
#
#
# class SupplierStockOfferAdmin(admin.ModelAdmin):
#     list_display = ('created_on', 'vendor', 'manufacturer', 'product', 'description', 'quantity', 'cost', 'date_code',
#                     'lead_time', 'spq_moq', 'package', 'valid_till', 'ex_works', 'remark')
#     list_filter = ('lead_time', 'ex_works', 'valid_till')
#     search_fields = ('vendor__name', 'manufacturer__name', 'product__name', 'description')
#
#
# admin.site.register(SpotOffer, SpotOfferAdmin)
# admin.site.register(VendorLeadTimeOffer, VendorLeadTimeOfferAdmin)
# admin.site.register(CustomerExcessOffer, CustomerExcessOfferAdmin)
# admin.site.register(CustomerLeadTimeOffer, CustomerLeadTimeOfferAdmin)
# admin.site.register(SupplierStockOffer, SupplierStockOfferAdmin)
#
#
# class CustomerPOItemsAdmin(admin.ModelAdmin):
#     list_display = ('customer_po', 'vendor', 'manufacturer', 'product', 'description', 'quantity', 'qc_status', )
#     list_filter = ('qc_status', 'customer_po',)
#     search_fields = ('vendor', 'product', 'manufacturer', 'customer_po',)
#
#
# class CustomerRFQItemsAdmin(admin.ModelAdmin):
#     list_display = ('customer_rfq', 'vendor', 'manufacturer', 'product', 'description', 'quantity', 'target_price', 'delivery_on')
#     list_filter = ('customer_rfq',)
#     search_fields = ('vendor', 'customer_part_number', 'product', 'manufacturer', 'customer_rfq',)
#
#
# class CustomerPOAdmin(admin.ModelAdmin):
#     list_display = ('po_number', 'po_status', 'customer', 'delivery_on', )
#     list_filter = ('po_status', 'delivery_on')
#     search_fields = ('po_number', 'po_status', 'customer__name', 'delivery_on')
#
#
# class CustomerRFQAdmin(admin.ModelAdmin):
#     list_display = ('rfq_number', 'rfq_status', 'customer', 'valid_till', )
#     list_filter = ('rfq_status', 'valid_till')
#     search_fields = ('rfq_number', 'rfq_status', 'customer__name', 'delivery_on')
#
#
# class CustomerPartNumberAdmin(admin.ModelAdmin):
#     list_display = ('part_number', 'customer',)
#
#
# admin.site.register(CustomerPO, CustomerPOAdmin)
# admin.site.register(CustomerPOItems, CustomerPOItemsAdmin)
# admin.site.register(CustomerRFQ, CustomerRFQAdmin)
# admin.site.register(CustomerRFQItems, CustomerRFQItemsAdmin)
# admin.site.register(CustomerPartNumber, CustomerPartNumberAdmin)
#
#
