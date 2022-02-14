from random import randint

num_suc = 0

for i in range(3):
    rand_num = randint(0,1)
    if rand_num == 1:
        num_suc += 1

print(num_suc)