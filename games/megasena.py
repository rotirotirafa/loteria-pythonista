import random


class Megasena:

    def __init__(self, game, default_quantity):
        self.game = game
        self.default_quantity = 6

    def create_new_game(self):
        return self.megasena

    def generator(self, maxLenght):
        return random.randrange(1, maxLenght)

    def checkLenghtOfSix(self, new_lucky_numbers):
        if len(new_lucky_numbers) < 6:
            return True
        return False

    def remove_repeated(self, lucky_numbers):
        new_lucky_numbers = []
        for number in lucky_numbers:
            if number not in new_lucky_numbers:
                new_lucky_numbers.append(number)
        while self.checkLenghtOfSix(new_lucky_numbers):
            new_lucky_numbers.append(self.generator(60))
        return sorted(new_lucky_numbers)

    def megasena(self):
        lucky_numbers = []
        for n in range(self.default_quantity):
            lucky_numbers.append(self.generator(60))
        return self.remove_repeated(lucky_numbers)

