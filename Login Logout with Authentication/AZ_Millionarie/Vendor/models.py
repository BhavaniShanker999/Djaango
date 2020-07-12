from django.db import models

# Create your models here.
class Vendormod(models.Model):
    Name=models.CharField(max_length=30)
    ShopName=models.CharField(max_length=30)
    Age=models.CharField(max_length=30)
    PhoneNo=models.CharField(max_length=30)
    AdharCard=models.CharField(max_length=30)
    PanCard=models.CharField(max_length=30)
    GSTNo=models.CharField(max_length=30)
    Mail=models.EmailField()
    Address=models.CharField(max_length=100)

    
