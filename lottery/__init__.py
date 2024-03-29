class Lottery:


    def __init__(self, name: str, bets: int, quantity: int, max_choices: int, min_choices: int) -> None:
        self.name = name
        self.bets = bets
        self.quantity = quantity
        self.max_choices = max_choices
        self.min_choices = min_choices

    def __repr__(self) -> str:
        return f'Name: {self.name}, Apostas: {self.bets}, Quantidade: {self.quantity}'


class Megasena(Lottery):
    pass


a = Megasena(name='megasena', bets=10, quantity=5, max_choices=15, min_choices=6).__repr__
print(a)