#type:ignore

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from ...models import Deposit, Wallet

def index(request):
    latest_deposit_list = Deposit.objects.all()
    context = {
        "latest_deposit_list": latest_deposit_list
    }
    return render(request, "belanjainaja/deposit/index.html", context=context)

def create(request):
    if request.method == 'POST':

        wallet = Wallet.objects.first()

        try:
            new_deposit = Deposit()
            new_deposit.saved_on = request.POST['saved_on']
            new_deposit.amount = int(request.POST['amount'])
            new_deposit.description = request.POST['description']

            wallet.income += int(request.POST['amount'])
            wallet.balance += int(request.POST['amount'])

            wallet.save()
            new_deposit.save()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:deposit.create"))
        
        return HttpResponseRedirect(reverse("belanja:deposit.index"))
    
    return render(request, "belanjainaja/deposit/create.html")

def update(request, deposit_id):
    deposit = get_object_or_404(Deposit, pk=deposit_id)
    
    if request.method == 'POST':

        try:
            deposit.saved_on = request.POST['saved_on']
            deposit.amount = request.POST['amount']
            deposit.description = request.POST['description']
            deposit.save()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:deposit.index"))
        
        return HttpResponseRedirect(reverse("belanja:deposit.index"))
    
    return render(request, "belanjainaja/deposit/update.html", context={"deposit": deposit})

def delete(request, deposit_id):
    if request.method == 'POST':

        deposit = get_object_or_404(Deposit, pk=deposit_id)

        try:
            deposit.delete()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:deposit.index"))
        
        return HttpResponseRedirect(reverse("belanja:deposit.index"))
    
    return render(request, "belanjainaja/deposit/create.html")

def init_wallet(request):
    wallet = Wallet.objects.first()

    if not wallet:
        wallet = Wallet()
        wallet.income = 0
        wallet.balance = 0
        wallet.expenditure = 0
        wallet.save()

    return HttpResponseRedirect(reverse("belanja:deposit.index"))
