import pytest

def test_shared_initial_balance(funded_account):
    assert funded_account.balance == 1000

def test_shared_withdraw(funded_account):
    funded_account.withdraw(500)
    assert funded_account.balance == 500
    