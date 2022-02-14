from random import randint

num_suc = 0
list_num_suc = []

for i in range(10):

    for i in range(3):
        rand_num = randint(0,1)
        if rand_num == 1:
            num_suc += 1

    list_num_suc.append(num_suc)
    num_suc = 0

print(list_num_suc)