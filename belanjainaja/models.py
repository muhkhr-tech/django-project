#type:ignore

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()

class Shopping(models.Model):
    purchase_date = models.DateField()
    description = models.CharField(max_length=500)
    total_price = models.BigIntegerField(default=0)
    is_verify = models.BooleanField(default=False)
    items = models.ManyToManyField(Item, through='ShoppingItem')

class ShoppingItem(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.BigIntegerField()
    unit = models.CharField(max_length=10)
    total_price = models.BigIntegerField()

class Wallet(models.Model):
    income = models.BigIntegerField()
    expenditure = models.BigIntegerField()
    balance = models.BigIntegerField()

class Deposit(models.Model):
    saved_on = models.DateField()
    amount = models.BigIntegerField()
    description = models.CharField(max_length=500, )

class Withdraw(models.Model):
    pulled_on = models.DateField()
    amount = models.BigIntegerField()
    description = models.CharField(max_length=500, )

