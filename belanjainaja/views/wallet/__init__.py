#type:ignore

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ...models import Deposit, Wallet

@login_required
def index(request):
    wallet = Wallet.objects.first()
    context = {
        "wallet": wallet
    }
    return render(request, "belanjainaja/wallet/index.html", context=context)