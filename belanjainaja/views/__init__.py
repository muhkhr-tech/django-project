#type:ignore

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models import *

@login_required
def index(request):
    return render(request, "belanjainaja/index.html")

@login_required
def init_wallet(request):
    wallet = Wallet.objects.first()

    if not wallet:
        wallet = Wallet()
        wallet.income = 0
        wallet.balance = 0
        wallet.expenditure = 0
        wallet.save()

    return HttpResponseRedirect(reverse("belanja:index"))

@login_required
def reset(request):
    items = Item.objects.all()
    deposit = Deposit.objects.all()
    withdraw = Withdraw.objects.all()
    wallet = Wallet.objects.first()
    shopping = Shopping.objects.all()
    shopping_item = ShoppingItem.objects.all()

    wallet.income = 0
    wallet.balance = 0
    wallet.expenditure = 0
    wallet.save()

    for item in items:
        item.delete()

    for item in deposit:
        item.delete()

    for item in withdraw:
        item.delete()

    for shop in shopping:
        shop.delete()

    for shop_item in shopping_item:
        shop_item.delete()

    context = {
        "message": {
            "type": "success",
            "text": "Data berhasil direset, silakan mulai mencoba aplikasi."
        }
    }

    return HttpResponseRedirect(reverse("belanja:index"))