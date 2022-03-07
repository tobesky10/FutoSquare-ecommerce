from django.contrib import admin
from ecomstore.models import User, Product, Message, Category, Cart
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Cart)

