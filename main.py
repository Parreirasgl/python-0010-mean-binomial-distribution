from random import randint

num_suc = 0
list_num_suc = []
total_suc = 0
num_simul = 10000

for i in range(num_simul):

    for i2 in range(3):
        rand_num = randint(0,1)
        if rand_num == 1:
            num_suc += 1

    list_num_suc.append(num_suc)
    num_suc = 0

for i3 in list_num_suc:
    total_suc = total_suc + i3

print(total_suc / num_simul)