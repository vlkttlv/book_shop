from django.contrib import admin
from shop.models import Customer, CartItem, Comment, Book, Address, Order, Category


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Address)
admin.site.register(Category)
