from email.policy import default
from django.db import models

# Create your models here.\



class drink_shop(models.Model):
  shop_id = models.IntegerField()
  shop_name = models.CharField(max_length=50) 
  shop_location = models.CharField(max_length=50)  
  shop_owner = models.CharField(max_length=50)  
  shop_contacts = models.CharField(max_length=10)  

  def __str__(self) :
    return str(self.shop_name)


class itisha_drinks(models.Model):
  drink_slug = models.CharField(max_length=250, primary_key=True, null=False, help_text = "the names of the product SHOULD be unique to every product.")  #this is a slugify design to map web pages amd identify products
  drink_type = models.CharField(max_length=250, null=False, blank=False, help_text = "this is the drink category, either alcohol, Energy drink, juice ...")
  drink_name = models.CharField(max_length=250, null=False, blank=False, help_text = "Can be same to drink slug, (but not every time)")  
  drink_qty = models.CharField(max_length=250, null=False, blank=False)
  drink_price = models.IntegerField()
  drink_description = models.CharField(max_length=250, null=False, blank=False)
  top_rated =models.BooleanField(default=False, help_text = "categorised under the top rated category")
  recommended =models.BooleanField(default=False, help_text = " recommencded to other users")
  offers =models.BooleanField(default=False, help_text = " categorised as 15% off")
  
  

  def __str__(self):
    return self.drink_name




###




  
