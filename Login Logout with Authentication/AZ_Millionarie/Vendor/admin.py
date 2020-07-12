from django.contrib import admin
from Vendor.models import Vendormod

# Register your models here.
class Vendormod_admin(admin.ModelAdmin):
    list_display=['Name','ShopName','Age','AdharCard','PanCard','GSTNo','PhoneNo','Mail']
admin.site.register(Vendormod,Vendormod_admin)
