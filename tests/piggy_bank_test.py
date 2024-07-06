
import pytest
import json
from piggy_bank import PiggyBank


@pytest.fixture
def setup():
    with open("./data/savings.json", "w") as f:
        json.dump({"amount": 10_000}, f)

def test_load():
    pb = PiggyBank()
    with open("./data/savings.json", "r") as f:
        savings = json.load(f)
    assert savings["amount"] == pb.savings

def test_save():
    pb = PiggyBank()
    test_amount = pb.savings + 5
    pb.savings = test_amount
    with open("./data/savings.json", "r") as f:
        savings = json.load(f)
    assert savings["amount"] == test_amount

def test_str():
    pb = PiggyBank()
    assert str(pb) == f"There are £{pb.savings} in this piggy bank."

def test_repr():
    pb = PiggyBank()
    assert repr(pb) == f"PiggyBank(savings={pb.savings})"

def test_set_negative():
    pb = PiggyBank()
    with pytest.raises(ValueError) as e:
        pb.savings = -1

def test_set_positive():
    pb = PiggyBank()
    pb.savings = 100_000_000
    assert pb.savings == 100_000_000

def test_add_negative():
    pb = PiggyBank()
    with pytest.raises(ValueError) as e:
        pb.add(-3)

def test_add_positive():
    pb = PiggyBank()
    test_amount = pb.savings
    pb.add(5)
    assert pb.savings == test_amount + 5

def test_remove_negative():
    pb = PiggyBank()
    with pytest.raises(ValueError):
        pb.remove(-3)

def test_remove_positive():
    pb = PiggyBank()
    test_amount = pb.savings
    pb.remove(5)
    assert pb.savings == test_amount - 5

def test_empty():
    pb = PiggyBank()
    pb.empty()
    assert pb.savings == 0

    