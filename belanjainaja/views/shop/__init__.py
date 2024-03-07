#type:ignore

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.db import IntegrityError

from ...models import Item, Shopping, Wallet, ShoppingItem

def index(request):
    latest_shop_list = Shopping.objects.all()
    context = {
        "latest_shop_list": latest_shop_list
    }
    return render(request, "belanjainaja/shop/index.html", context=context)

def create(request):
    latest_item_list = Item.objects.all()
    
    context = {
        "latest_item_list": latest_item_list
    }

    if request.method == 'POST':

        wallet = Wallet.objects.first()

        split_item_id_and_price = request.POST['item_id'].split('`')
        item_id = split_item_id_and_price[0]

        item = get_object_or_404(Item, pk=item_id)
        
        try:
            new_shop = Shopping()
            new_shop.purchase_date = request.POST['purchase_date']
            new_shop.description = request.POST['description']

            total_price = int(request.POST['price']) * int(request.POST['quantity'])

            new_shop_item = ShoppingItem()
            new_shop_item.shopping = new_shop
            new_shop_item.item = item
            new_shop_item.price = request.POST['price']
            new_shop_item.quantity = request.POST['quantity']
            new_shop_item.unit = request.POST['unit']
            new_shop_item.total_price = total_price

            wallet.expenditure += total_price
            wallet.balance -= total_price

            wallet.save()
            new_shop.save()
            new_shop_item.save()
        except IntegrityError:
            print('erererorororo')
            return HttpResponseRedirect(reverse("belanja:shop.create"))
        
        return HttpResponseRedirect(reverse("belanja:shop.add_item", kwargs={'shop_id': new_shop.id}))
    
    return render(request, "belanjainaja/shop/create.html", context=context)

def add_item(request, shop_id):
    latest_item_list = Item.objects.all()
    
    shop = get_object_or_404(Shopping, pk=shop_id)

    shopping_item = ShoppingItem.objects.filter(shopping=shop)

    context = {
        "shop": shop,
        "shopping_item": shopping_item,
        "latest_item_list": latest_item_list
    }

    if request.method == 'POST':

        wallet = Wallet.objects.first()

        split_item_id_and_price = request.POST['item_id'].split('`')
        item_id = split_item_id_and_price[0]

        item = get_object_or_404(Item, pk=item_id)

        shop = get_object_or_404(Shopping, pk=shop_id)
        
        try:
            total_price = int(request.POST['price']) * int(request.POST['quantity'])

            shop_item = ShoppingItem.objects.filter(shopping=shop, item=item)

            if shop_item:
                shop_item[0].price = request.POST['price']
                shop_item[0].quantity = request.POST['quantity']
                shop_item[0].unit = request.POST['unit']
                shop_item[0].total_price = total_price

                shop_item[0].save()

            else:
                new_shop_item = ShoppingItem()
                new_shop_item.shopping = shop
                new_shop_item.item = item
                new_shop_item.price = request.POST['price']
                new_shop_item.quantity = request.POST['quantity']
                new_shop_item.unit = request.POST['unit']
                new_shop_item.total_price = total_price

                new_shop_item.save()

            wallet.expenditure += total_price
            wallet.balance -= total_price

            wallet.save()
            shop.save()

        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:shop.add_item", kwargs={'shop_id': shop_id}))
        
        return HttpResponseRedirect(reverse("belanja:shop.add_item", kwargs={'shop_id': shop_id}))
    
    return render(request, "belanjainaja/shop/add-item.html", context=context)

def detail(request, shop_id):
    latest_item_list = Item.objects.all()
    
    shop = get_object_or_404(Shopping, pk=shop_id)

    shopping_item = ShoppingItem.objects.filter(shopping=shop)

    context = {
        "shop": shop,
        "shopping_item": shopping_item,
        "latest_item_list": latest_item_list
    }
    
    return render(request, "belanjainaja/shop/detail.html", context=context)

def update(request, shop_id):
    shop = get_object_or_404(Shopping, pk=shop_id)
    
    if request.method == 'POST':

        try:
            shop.saved_on = request.POST['saved_on']
            shop.amount = request.POST['amount']
            shop.description = request.POST['description']
            shop.save()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:shop.index"))
        
        return HttpResponseRedirect(reverse("belanja:shop.index"))
    
    return render(request, "belanjainaja/shop/update.html", context={"shop": shop})

def delete(request, shop_id):
    shop = get_object_or_404(Shopping, pk=shop_id)

    shopping_item = get_list_or_404(ShoppingItem, shopping=shop)

    if request.method == 'POST':

        wallet = Wallet.objects.first()
        
        try:
            for shopping in shopping_item:
                wallet.expenditure -= shopping.total_price
                wallet.balance += shopping.total_price

            wallet.save()
            shop.delete()
            shopping.delete()

        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:shop.index"))
        
        return HttpResponseRedirect(reverse("belanja:shop.index"))
    
    return HttpResponseNotFound()

def init_wallet(request):
    wallet = Wallet.objects.first()

    if not wallet:
        wallet = Wallet()
        wallet.income = 0
        wallet.balance = 0
        wallet.expenditure = 0
        wallet.save()

    return HttpResponseRedirect(reverse("belanja:shop.index"))
