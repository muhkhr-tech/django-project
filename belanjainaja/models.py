#type:ignore

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()

class Shopping(models.Model):
    purchase_date = models.DateField()
    description = models.CharField(max_length=500, )
    items = models.ManyToManyField(Item)

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

