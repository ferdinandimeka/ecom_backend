from django.contrib import admin
from .models import Product, Review, Order, OrderItem, ShippingAddress, Transaction, Categories

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'isPaid', 'paidAt', 'isDelivered', 'deliveredAt', 'totalPrice', 'createdAt'
        ]

@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'transaction_id', 'amount', 'status', 'created_at'
        ]
    
admin.register(Categories)