from django.test import TestCase
from accounting.models import Account, Currency
# Create your tests here.


class TestAccountTransaction(TestCase):
    #fixtures = ['userx.xml', 'account.xml']

    def setUp(self):
        self.currency1 = Currency.objects.create(name="currency1")
        self.currency2 = Currency.objects.create(name="currency2")

        self.account1 = Account.objects.create(
            amount=25, currency=self.currency2)

        self.account2 = Account.objects.create(
            amount=0,  currency=self.account1.currency)

    def test_transaction_succed(self):
        # user=
        self.account1.withdraw(10, self.account2)
        self.assertEquals(self.account1.amount, 15)
        self.assertEquals(self.account2.amount, 10)

    def test_transaction_whith_enough_money_fails(self):
        self.assertRaises(
            AssertionError, self.account1.withdraw, 100, self.account2)
