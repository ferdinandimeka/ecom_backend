from django.db import models
from django.contrib.auth.models import User
import random, string

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return (self.name)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(Categories, null=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return (self.name)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return (self.rating)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        # Call the parent class's save method
        super(Order, self).save(*args, **kwargs)

        # create or update a new transaction object
        if self.isPaid and not self.transaction_set.exists():
            transaction = Transaction.objects.create(
                user=self.user,
                order=self,
                amount=self.totalPrice,
                payment_method=self.paymentMethod,
                status='Completed',
                transaction_id=self.generate_transaction_id()
            )

        if not self.transaction_set.exists():
            transaction = Transaction.objects.create(
                user=self.user,
                order=self,
                amount=self.totalPrice,
                payment_method=self.paymentMethod,
                status='Pending',  # Default status for a pending order
                transaction_id=self.generate_transaction_id()
            )

    def generate_transaction_id(self):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return f"#{self._id}-{random_string}"

    def __str__(self):
        return str(self.createdAt)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return (self.name)

class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self):
        return (self.address)
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=200, default='Pending')
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self):
        return f"Transaction {self._id} - {self.status}"