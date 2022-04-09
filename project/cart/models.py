from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from store.models import Product, Variation
from accounts.models import Account

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __int__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    variations = models.ManyToManyField(Variation,blank=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    quantity =  models.IntegerField()
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def sub_total(self):
        return self.product.price * self.quantity


    def __unicode__(self):
        return self.product 