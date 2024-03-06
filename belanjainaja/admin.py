#type:ignore

from django.contrib import admin

from .models import *

admin.site.register(Item)
admin.site.register(Shopping)
admin.site.register(Wallet)
admin.site.register(Deposit)
admin.site.register(Withdraw)
