from email.policy import default
from django.db import models

# Create your models here.\


ALCOHOL_CATEGORY = (
    ('G', 'Gin'),
    ('W', 'Whiskey'),
    ('V', 'Vodka'),
    ('R', 'Ram'),
    
)

DRINK_CATEGORY = (
    ('S', 'Soda'),
    ('C', 'CockTails'),
    ('J', 'Juices'),
    ('Y', 'Yorghurt'),
    
)


##Model for alcohol============================================

class alcohol_drinks(models.Model):
  drink_slug = models.CharField(max_length=250, primary_key=True, null=False, help_text = "the names of the product SHOULD be unique to every product.")  #this is a slugify design to map web pages amd identify products
  drink_type = models.CharField(choices=ALCOHOL_CATEGORY, max_length=20)
  drink_name = models.CharField(max_length=250, null=False, blank=False, help_text = "Can be same to drink slug, (but not every time)")  
  drink_qty = models.CharField(max_length=250, null=False, blank=False)
  drink_price = models.IntegerField()
  #alcohol_drinks_type = models.CharField(choices=ALCOHOL_CATEGORY, max_length=20)
  drink_description = models.CharField(max_length=250, null=False, blank=False)
  top_rated =models.BooleanField(default=False, help_text = "categorised under the top rated category")
  recommended =models.BooleanField(default=False, help_text = " recommencded to other users")
  offers =models.BooleanField(default=False, help_text = " categorised as 15% off")
  
  
  #the name to display in django admin
  def __str__(self):
    return self.drink_name

    

##Model for sodas, energyy drinks, coctailsl============================================

class itisha_drinks(models.Model):
  drink_slug = models.CharField(max_length=250, primary_key=True, null=False, help_text = "the names of the product SHOULD be unique to every product.")  #this is a slugify design to map web pages amd identify products
  drink_type = models.CharField(choices=DRINK_CATEGORY, max_length=20)
  drink_name = models.CharField(max_length=250, null=False, blank=False, help_text = "Can be same to drink slug, (but not every time)")  
  drink_qty = models.IntegerField( help_text = "the amount of drinks in store. Eg  25 ")
  drink_price = models.IntegerField()
  drink_description = models.CharField(max_length=250, null=False, blank=False)
  top_rated =models.BooleanField(default=False, help_text = "categorised under the top rated category")
  recommended =models.BooleanField(default=False, help_text = " recommencded to other users")
  offers =models.BooleanField(default=False, help_text = " categorised as 15% off")
  
  
#the name to display in django admin
  def __str__(self):
    return self.drink_name





## tHis view should store information about the store, I will improve the view to become a CRM to manage the drinks

class drink_shop(models.Model):
  shop_id = models.IntegerField()
  shop_name = models.CharField(max_length=50) 
  shop_location = models.CharField(max_length=50)  
  shop_owner = models.CharField(max_length=50)  
  shop_contacts = models.CharField(max_length=10)  

  #the name to display in django admin
  def __str__(self) :
    return str(self.shop_name)







  
