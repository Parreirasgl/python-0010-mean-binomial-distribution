# I've learned how to calculate the mean of a binomial distribution.
# I've calculated that the mean of a binomial distribution,
# in the case of 3 flips of a coin, is 1.5.
# I decided to do a simulation to prove that result.

# Aprendi a calcular a média de uma distribuição binomial.
# Calculei que a média da distribuição binomial,
# no caso de 3 lançamentos de uma moeda, é 1.5.
# Resolvi fazer uma simulação para comprovar esse resultado.

from random import randint

number_successes = 0
list_number_successes = []
total_successes = 0
number_simulations = 10000

for i in range(number_simulations):

    for i2 in range(3):
        random_number = randint(0, 1)
        if random_number == 1:
            number_successes += 1

    list_number_successes.append(number_successes)
    number_successes = 0

for i3 in list_number_successes:
    total_successes = total_successes + i3

print(total_successes / number_simulations)
