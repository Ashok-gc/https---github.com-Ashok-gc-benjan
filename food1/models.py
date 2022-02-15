from django.db import models

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
    



