#type:ignore

from django.test import TestCase

from ...models import Wallet

class ModelWallet(TestCase):
    def test_has_minimal_one_row(self):
        init_wallet = Wallet.objects.all()

        self.assertEqual(len(init_wallet), 1)