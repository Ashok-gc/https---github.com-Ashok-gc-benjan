from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=100,blank=True)
    email=models.CharField(max_length=100,blank=True)
    number=models.CharField(max_length=10,blank=True)
    password=models.CharField(max_length=100,blank=True)

    class Meta:

        db_table="customer"


class catering(models.Model):
    catering_id=models.AutoField(auto_created=True,primary_key=True)
    c_Name=models.CharField(max_length=100,blank=True)
    c_number=models.CharField(max_length=100,blank=True)
    c_types=models.CharField(max_length=100,blank=True)
    c_p_number=models.CharField(max_length=100,blank=True)
    c_date=models.DateTimeField(blank=True)
    c_address=models.CharField(max_length=100,blank=True)
    c_details=models.CharField(max_length=100,blank=True)

    class Meta:

        db_table="catering"
