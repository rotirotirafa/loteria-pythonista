import random


def generator(max_lenght):
    return random.randrange(1, max_lenght)


def check_six_size(new_lucky_numbers):
    if len(new_lucky_numbers) < 6:
        return True
    return False


def remove_repeated(lucky_numbers):
    new_lucky_numbers = []
    
    for number in lucky_numbers:
        if number not in new_lucky_numbers:
            new_lucky_numbers.append(number)

    while check_six_size(new_lucky_numbers):
        new_lucky_numbers.append(generator(60))

    return sorted(new_lucky_numbers)


def megasena(numbers_quantity: int = 6):

    if numbers_quantity > 15:
        numbers_quantity = 15

    lucky_numbers = []

    for n in range(numbers_quantity):
        lucky_numbers.append(generator(60))

    return remove_repeated(lucky_numbers)

def multiple_luckynumbers(bets: int, numbers_quantity: int):
    lucky_numbers = []
    
    for n in range(bets):
        lucky_numbers.append({"game": n, "numbers": megasena(numbers_quantity)})
    
    return lucky_numbers

print(multiple_luckynumbers(1,6))