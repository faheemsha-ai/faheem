from django.contrib import admin
from .models import Product , CartItem , Address

admin.site.register(Product)
admin.site.register(Address)
admin.site.register(CartItem)
