from django.db import models

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

class order(models.Model):
    order_id = models.AutoField
    product_id = models.ForeignKey('product',on_delete = models.CASCADE)
    payment_status = models.CharField(max_length = 100)
    total_order_amt = models.FloatField()
    order_status = models.CharField(max_length = 100)
    delivery_address = models.CharField(max_length= 100)
    order_place_date = models.TimeField(auto_now = True, auto_now_add = False)

class profile(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length = 100)
    user_address = models.CharField(max_length = 100)
    user_email = models.EmailField(max_length = 254)
    user_phone = models.CharField(max_length = 14)
    user_balance = models.FloatField()
    profile_pic = models.ImageField(upload_to = 'media')
    user_orders = models.ForeignKey('order',on_delete = models.CASCADE)
    profile_creation_date = models.TimeField(auto_now = True, auto_now_add = False)