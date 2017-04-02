from django.db import models
from django.contrib.auth.models import User
import datetime

class User_Data(models.Model):

    USER = 'user'
    ADMIN = 'admin'
    
    ROL_CHOICES = (
        (USER, 'USER'),
        (ADMIN, 'ADMIN'),
    )
    
    tagRfid = models.CharField(max_length=64, blank=False)
    chatid = models.DecimalField(max_digits=12, decimal_places=0)
    balance_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    username = models.CharField(max_length=20, blank=False)
    user = models.ForeignKey(User)
    rol = models.CharField(max_length=5,
                                      choices=ROL_CHOICES,
                                      default=USER,
                                      blank=False,
                                      )


class Balance(models.Model):

    CASH = 'cash'
    PAYPAL = 'PayPal'
    
    TYPE_PAYMENT = (
        (CASH, 'CASH'),
        (PAYPAL, 'PAYPAL'),
    )
    
    user = models.ForeignKey(User_Data, blank=False)
    amount_entered = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=False)
    type_amount = models.CharField(max_length=5,
                                      choices=TYPE_PAYMENT,
                                      default=CASH,
                                      blank=False,
                                      )
    date = models.DateTimeField( default=datetime.datetime.now() )


#Artíclo
class Item(models.Model):

    name = models.CharField(max_length=30, blank=False)
    barcode = models.CharField(max_length=30, blank=False)
    price_sale = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    stock = models.IntegerField(blank=False)
    
    
class Shopping_History(models.Model):

    item = models.ForeignKey(Item, blank=False)
    date = models.DateTimeField( default=datetime.datetime.now() )
    units = models.IntegerField(default=0)
    unit_purchase_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    supermarket = models.CharField(max_length=30)
    
    
class Sale_History(models.Model):

    item = models.ForeignKey(Item, blank=False)
    date = models.DateTimeField( default=datetime.datetime.now() )
    price_sale = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price_cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
## COMPROBAR que campos son necesarios #, blank=False