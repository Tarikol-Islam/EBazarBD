from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length= 30)
    product_desc = models.TextField(max_length = 400, default= None)
    product_catg = models.CharField(max_length = 100)
    product_brand = models.CharField(max_length = 20)
    product_price = models.FloatField()
    product_pic = models.ImageField(upload_to='Shop/Images', default="")
    product_qty = models.IntegerField()
    product_creation_date = models.TimeField(auto_now = True, auto_now_add = False)
    
    def __str__(self):
        return self.product_name

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField(max_length=14, default="")

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key = True)
    order_id =models.IntegerField(default="")
    update_desc = models.CharField(max_length= 5000)
    timestamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_desc[0:7]+"..."
        
class profile(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length = 100)
    user_address = models.CharField(max_length = 100)
    user_email = models.EmailField(max_length = 254)
    user_phone = models.CharField(max_length = 14)
    user_balance = models.FloatField()
    profile_pic = models.ImageField(upload_to = 'media')
    profile_creation_date = models.TimeField(auto_now = True, auto_now_add = False)