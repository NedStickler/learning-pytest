
import json

class PiggyBank:
    def __init__(self) -> None:
        with open("./data/savings.json", "r") as f:
           savings = json.load(f)
        self.__savings = savings["amount"]
    
    def __str__(self) -> str:
        return f"There are £{self.__savings} in this piggy bank."

    def __repr__(self) -> str:
        return f"PiggyBank(savings={self.savings})"
    
    def _save(self) -> None:
        with open("./data/savings.json", "w") as f:
            json.dump({"amount": self.__savings}, f)

    @property
    def savings(self) -> float:
        return self.__savings
    
    @savings.setter
    def savings(self, savings: float) -> None:
        if savings < 0:
            raise ValueError("Cannot set savings to a negative value.")
        self.__savings = savings
        self._save()
    
    def add(self, add: float) -> None:
        if add < 0:
            raise ValueError("Cannot add a negative amount.")
        self.__savings += add
        self._save()
    
    def remove(self, remove: float) -> None:
        if remove < 0:
            raise ValueError("Cannot remove a negative amount.")
        if self.__savings - remove < 0:
            raise ValueError(f"Insufficient funds to remove £{remove}.")
        self.__savings -= remove
        self._save()
    
    def empty(self) -> None:
        self.__savings = 0
        self._save()
