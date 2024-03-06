#type:ignore

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from ...models import Withdraw, Wallet

def index(request):
    latest_withdraw_list = Withdraw.objects.all()
    context = {
        "latest_withdraw_list": latest_withdraw_list
    }
    return render(request, "belanjainaja/withdraw/index.html", context=context)

def create(request):
    if request.method == 'POST':

        wallet = Wallet.objects.first()

        try:
            new_withdraw = Withdraw()
            new_withdraw.pulled_on = request.POST['pulled_on']
            new_withdraw.amount = int(request.POST['amount'])
            new_withdraw.description = request.POST['description']

            wallet.expenditure += int(request.POST['amount'])
            wallet.balance -= int(request.POST['amount'])

            wallet.save()
            new_withdraw.save()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:withdraw.create"))
        
        return HttpResponseRedirect(reverse("belanja:withdraw.index"))
    
    return render(request, "belanjainaja/withdraw/create.html")

def update(request, withdraw_id):
    withdraw = get_object_or_404(Withdraw, pk=withdraw_id)
    
    if request.method == 'POST':

        try:
            withdraw.pulled_on = request.POST['pulled_on']
            withdraw.amount = request.POST['amount']
            withdraw.description = request.POST['description']
            withdraw.save()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:withdraw.index"))
        
        return HttpResponseRedirect(reverse("belanja:withdraw.index"))
    
    return render(request, "belanjainaja/withdraw/update.html", context={"withdraw": withdraw})

def delete(request, withdraw_id):
    if request.method == 'POST':

        withdraw = get_object_or_404(Withdraw, pk=withdraw_id)

        try:
            withdraw.delete()
        except IntegrityError:
            return HttpResponseRedirect(reverse("belanja:withdraw.index"))
        
        return HttpResponseRedirect(reverse("belanja:withdraw.index"))
    
    return render(request, "belanjainaja/withdraw/create.html")