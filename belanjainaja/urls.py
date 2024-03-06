#type:ignore

from django.urls import path

from .views import item, deposit, wallet, withdraw

app_name='belanja'

urlpatterns = [
    path("item/", item.index, name="item.index"),
    path("item/create/", item.create, name="item.create"),
    path("item/<int:item_id>/update/", item.update, name="item.update"),
    path("item/<int:item_id>/delete/", item.delete, name="item.delete"),
    path("item/reset/", item.reset, name="item.reset"),

    path("deposit/", deposit.index, name="deposit.index"),
    path("deposit/create/", deposit.create, name="deposit.create"),
    path("deposit/<int:deposit_id>/update/", deposit.update, name="deposit.update"),
    path("deposit/<int:deposit_id>/delete/", deposit.delete, name="deposit.delete"),
    path("deposit/init-wallet/", deposit.init_wallet, name="deposit.init-wallet"),

    path("wallet/", wallet.index, name="wallet.index"),

    path("withdraw/", withdraw.index, name="withdraw.index"),
    path("withdraw/create/", withdraw.create, name="withdraw.create"),
    path("withdraw/<int:withdraw_id>/update/", withdraw.update, name="withdraw.update"),
    path("withdraw/<int:withdraw_id>/delete/", withdraw.delete, name="withdraw.delete"),
]