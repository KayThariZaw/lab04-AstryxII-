import pytest
from bank import BankAccount

@pytest.fixture
def setup_teardown_account():
    print("[setup]")
    acc = BankAccount(100)
    yield acc
    print("[teardown]")

def test_teardown_one(setup_teardown_account):
    setup_teardown_account.deposit(50)
    assert setup_teardown_account.balance == 150

def test_teardown_two(setup_teardown_account):
    setup_teardown_account.withdraw(20)
    assert setup_teardown_account.balance == 80
    
