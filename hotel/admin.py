from django.contrib import admin
from .models import Customer, Staff, Food, Order, Comment, Data, OrderContent, Cart, DeliveryBoy, Contact

admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(Comment)
admin.site.register(Data)
admin.site.register(DeliveryBoy)
admin.site.register(OrderContent)
admin.site.register(Cart)
admin.site.register(Contact)