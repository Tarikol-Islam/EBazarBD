from django.contrib import admin
from .models import OrderUpdate, Orders, profile,product,OrderUpdate
# Register your models here.
admin.site.register(profile)
admin.site.register(Orders)
admin.site.register(product)
admin.site.register(OrderUpdate)