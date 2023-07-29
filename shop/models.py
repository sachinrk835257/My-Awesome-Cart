from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default=" not available")
    sub_category = models.CharField(max_length=80, default="not available")
    price = models.IntegerField(default=0.0)
    desc = models.CharField(max_length=600)
    pub_date = models.DateField()
    product_image = models.ImageField(upload_to="shop/images", default="not found")         # should be added media directory in settings.py

    def __str__(self):
        return self.product_name           # return the product name in our admin page 
    
class contact(models.Model):
    query_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50,default="nil")
    email = models.CharField(max_length=70, default=" not available")
    phone = models.IntegerField(default=00000)
    desc = models.CharField(max_length=600)
    date = models.DateField()
    # product_image = models.ImageField(upload_to="shop/images", default="not found")         # should be added media directory in settings.py

    def __str__(self):
        return self.user          # return the product name in our admin page 

class yourCart(models.Model):
    product_id = models.AutoField(primary_key=True)
    items = models.TextField(default=" ")
    # quantity = models.TextField(max_length=10,default="1")
    
    def __str__(self):
        return self.items[0:15] + "..."            # return the product name in our admin page 

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000,default=" ")
    name = models.CharField(max_length=500,default="nil")
    email = models.CharField(max_length=700, default=" not available")
    phone = models.IntegerField()
    address = models.TextField(max_length=1500)
    state = models.CharField(max_length=500,default="null")
    city = models.CharField(max_length=700, default=" not available")
    zip = models.CharField(max_length=700, default=" not available")
    
    # product_image = models.ImageField(upload_to="shop/images", default="not found")         # should be added media directory in settings.py

    def __str__(self):
        return self.name
    
class orderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    update_desc = models.CharField(max_length=5000)
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:20]
    
class demo(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(auto_now_add=True)