#type:ignore

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from ...models import Deposit, Wallet

def index(request):
    wallet = Wallet.objects.first()
    context = {
        "wallet": wallet
    }
    return render(request, "belanjainaja/wallet/index.html", context=context)