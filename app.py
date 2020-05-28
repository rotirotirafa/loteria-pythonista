import random

def generator(maxLenght):
  return random.randrange(1, maxLenght)

def remove_repeated(lucky_numbers):
    new_lucky_numbers = []
    for number in lucky_numbers:
        if number not in new_lucky_numbers:
            new_lucky_numbers.append(number)
    while len(new_lucky_numbers) < 6:
      new_lucky_numbers.append(generator(60))
    return sorted(new_lucky_numbers)

def megasena():
  lucky_numbers = []
  for n in range(6):
    lucky_numbers.append(generator(60))
  return remove_repeated(lucky_numbers)

#retorna 1 conjunto de números da sorte para megasena
print(megasena())

#retorna x conjuntos de números da sorte para megasena
def multiple_luckynumbers():
  lucky_numbers = []
  for n in range(200):
    lucky_numbers.append({"Jogo": n, "números": megasena()})
  return lucky_numbers

#print(multiple_luckynumbers())