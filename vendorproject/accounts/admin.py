from django.contrib import admin
from .models import *
# Register your models here.

class customer_model_admin(admin.ModelAdmin):
    list_display=['name','phone','mail','address','date_created']
admin.site.register(customer_model,customer_model_admin,)

class product_model_admin(admin.ModelAdmin):
    list_display=['name','price','category','description','date_created']
admin.site.register(Product_model,product_model_admin)

class order_model_admin(admin.ModelAdmin):
    list_display=['customer_mod','products_mod','date_created','status']

admin.site.register(order_model,order_model_admin)

admin.site.register(tag_model)