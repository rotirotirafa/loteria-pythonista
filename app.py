import random


def generator(maxLenght):
    return random.randrange(1, maxLenght)


def checkLenghtOfSix(new_lucky_numbers):
    if len(new_lucky_numbers) < 6:
        return True
    return False


def remove_repeated(lucky_numbers):
    new_lucky_numbers = []
    for number in lucky_numbers:
        if number not in new_lucky_numbers:
            new_lucky_numbers.append(number)
    while checkLenghtOfSix(new_lucky_numbers):
        new_lucky_numbers.append(generator(60))
    return sorted(new_lucky_numbers)


def megasena():
    lucky_numbers = []
    for n in range(6):
        lucky_numbers.append(generator(60))
    return remove_repeated(lucky_numbers)

# retorna 1 conjunto de números da sorte para megasena
# print(megasena())


# retorna x conjuntos de números da sorte para megasena
def multiple_luckynumbers(quantity):
    lucky_numbers = []
    for n in range(quantity):
        lucky_numbers.append({"Jogo": n, "números": megasena()})
    return lucky_numbers

# print(multiple_luckynumbers(10))
