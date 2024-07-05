
import json

class PiggyBank:
    def __init__(self) -> None:
        with open("./data/savings.json", "r") as f:
           savings = json.load(f)
        self.__savings = savings["amount"]
    
    def __str__(self) -> str:
        return f"There are {self.__savings} in this piggy bank."

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
        self.__savings = savings
        self._save()
    
    def add(self, add: float) -> None:
        self.__savings += add
        self._save()
    
    def remove(self, remove: float) -> None:
        self.__savings -= remove
        self._save()
    
    def empty(self) -> None:
        self.__savings = 0
        self._save()
    
if __name__ == "__main__":
    pb = PiggyBank()
    print(str(pb))