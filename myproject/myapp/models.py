from django.db import models

# Create your models here.

class Order(models.Model):
    identifier = models.TextField(unique = True)
    created_at = models.DateField()
    vendor_id = models.DecimalField(decimal_places = 0, max_digits=10)
    customer_id = models.DecimalField(decimal_places = 0, max_digits=10)

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.DecimalField(decimal_places = 0, max_digits = 10)
    product_description = models.CharField(max_length = 255)
    product_price = models.DecimalField(decimal_places = 10, max_digits = 20)
    product_vat_rate = models.DecimalField(decimal_places = 10, max_digits = 20)
    discount_rate = models.DecimalField(decimal_places = 10, max_digits = 20)
    quantity = models.DecimalField(decimal_places = 0, max_digits = 10)
    full_price_amount = models.DecimalField(decimal_places = 10, max_digits = 20)
    discounted_amount = models.DecimalField(decimal_places = 10, max_digits = 20)
    vat_amount = models.DecimalField(decimal_places = 10, max_digits = 20)
    total_amount = models.DecimalField(decimal_places = 10, max_digits = 20)
