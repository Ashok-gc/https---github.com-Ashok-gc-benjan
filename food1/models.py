import imp
from django.db import models
from customer.models import Customer
from django.contrib.auth.models import User
import customer

# Create your models here.
class Food1(models.Model):
    food1_id=models.AutoField(auto_created=True,primary_key=True)
    Name=models.CharField(max_length=100)
    Price=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    Photo=models.FileField(upload_to="food_images")

    class Meta:

        db_table="food1"


# class catering(models.Model):
#     catering_id=models.AutoField(auto_created=True,primary_key=True)
#     c_Name=models.CharField(max_length=100)
#     c_number=models.CharField(max_length=100)
#     c_types=models.CharField(max_length=100)
#     c_p_number=models.CharField(max_length=100)
#     c_date=models.FileField(max_length=100)
#     c_address=models.CharField(max_length=100)
#     c_details=models.CharField(max_length=100)

#     class Meta:

#         db_table="cetering"



class Cart(models.Model):


    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Food1, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price

    def __unicode__(self):
        return self.product

