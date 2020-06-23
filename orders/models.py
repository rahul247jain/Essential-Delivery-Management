from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from shop.models import Product
# Create your models here.

CITY_CHOICES = (
    ('Ahmedabad', 'Ahmedabad'),
    ('Bengaluru', 'Bengaluru'),
    ('Chennai', 'Chennai'),
    ('Chittorgarh', 'Chittorgarh'),
    ('Jodhpur', 'Jodhpur'),
    ('Raipur', 'Raipur'),
    ('Sirohi', 'Sirohi'),
    ('Pali', 'Pali'),
    ('Delhi', 'Delhi'),
    ('Hyderabad', 'Hyderabad'),
    ('Kanpur', 'Kanpur'),
    ('Kolkata', 'Kolkata'),
    ('Mumbai', 'Mumbai'),
    ('Ratnagiri', 'Ratnagiri'),
    ('Pune', 'Pune'),
    ('Surat', 'Surat'),
    ('Sultanpur', 'Sultanpur'),
    ('Lucknow', 'Lucknow'),
    ('Patna', 'Patna'),
    ('Indore', 'Indore'),
    ('Vadodara', 'Vadodara'),
    ('Bhopal', 'Bhopal'),
    ('Coimbatore', 'Coimbatore'),
    ('Agra', 'Agra'),
    ('Meerut', 'Meerut'),
    ('Madurai', 'Madurai'),
    ('Guwahati', 'Guwahati'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Tiruchchirappalli', 'Tiruchchirappalli'),
    ('Kota', 'Kota'),
    ('Jammu', 'Jammu'),
    ('Mangalore', 'Mangalore'),
    ('Ajmer', 'Ajmer'),
    ('Shillong', 'Shillong'),
    ('New Delhi', 'New Delhi')
)


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user', null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price*self.quantity
