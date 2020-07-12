from django.forms import ModelForm
from .models import *

class create_order_form(ModelForm):
    class Meta:
        model= order_model
        fields='__all__'

class add_product_form(ModelForm):
    class Meta:
        model=Product_model
        fields='__all__'
        