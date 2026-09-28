import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_withdraw_decreases_balance(account):
    account.withdraw(40)
    assert account.balance == 60


def test_withdraw_overdraft_raises_error(account):
    with pytest.raises(ValueError):
        account.withdraw(150)