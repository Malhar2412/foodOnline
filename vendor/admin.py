from django.contrib import admin
from vendor.models import Vendor



class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'vendor_license', 'is_approved')
    list_display_links = ('user', 'vendor_name',) 


admin.site.register(Vendor)
