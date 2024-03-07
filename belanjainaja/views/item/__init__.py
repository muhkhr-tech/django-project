#type:ignore

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from ...models import Item, Deposit, Withdraw, Wallet, Shopping, ShoppingItem

def index(request):
    latest_item_list = Item.objects.all()
    context = {
        "latest_item_list": latest_item_list
    }
    return render(request, "belanjainaja/item/index.html", context=context)

def create(request):
    if request.method == 'POST':

        try:
            new_item = Item()
            new_item.name = request.POST['name']
            new_item.price = request.POST['price']
            new_item.save()
        except IntegrityError:
            return render(request, "belanjainaja/item/create.html")
        
        return HttpResponseRedirect(reverse("belanja:item.index"))
    
    return render(request, "belanjainaja/item/create.html")

def update(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.method == 'POST':

        try:
            item.name = request.POST['name']
            item.price = request.POST['price']
            item.save()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:item.index"))
        
        return HttpResponseRedirect(reverse("belanja:item.index"))
    
    return render(request, "belanjainaja/item/update.html", context={"item": item})

def delete(request, item_id):
    if request.method == 'POST':

        item = get_object_or_404(Item, pk=item_id)

        try:
            item.delete()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:item.index"))
        
        return HttpResponseRedirect(reverse("belanja:item.index"))
    
    return render(request, "belanjainaja/item/create.html")

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

    return HttpResponseRedirect(reverse("belanja:item.index"))
