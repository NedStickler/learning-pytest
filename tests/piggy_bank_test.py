
import json
from piggy_bank import PiggyBank


def test_json_load():
    pb = PiggyBank()
    with open("./data/savings.json", "r") as f:
        savings = json.load(f)
    assert savings["amount"] == pb.savings

def test_str_dunder():
    pb = PiggyBank()
    assert str(pb) == f"There are {pb.savings} in this piggy bank."