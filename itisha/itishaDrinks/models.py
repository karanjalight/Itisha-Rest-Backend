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
  drink_id = models.IntegerField(null=False)
  drink_name = models.CharField(max_length=250, null=False, blank=False)
  drink_type = models.CharField(max_length=250, null=False, blank=False)
  drink_qty = models.CharField(max_length=250, null=False, blank=False)
  drink_price = models.IntegerField()
  drink_description = models.CharField(max_length=250, null=False, blank=False)
  #shop = models.CharField(max_length=250, null=False, blank=False)  
  shops = models.ForeignKey(drink_shop, on_delete=models.CASCADE)

  def __str__(self):
    return self.drink_name


  
