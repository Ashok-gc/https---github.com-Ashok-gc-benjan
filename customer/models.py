from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:

        db_table="customer"


class catering(models.Model):
    catering_id=models.AutoField(auto_created=True,primary_key=True)
    c_Name=models.CharField(max_length=100)
    c_number=models.CharField(max_length=100)
    c_types=models.CharField(max_length=100)
    c_p_number=models.CharField(max_length=100)
    c_date=models.DateTimeField()
    c_address=models.CharField(max_length=100)
    c_details=models.CharField(max_length=100)

    class Meta:

        db_table="catering"
