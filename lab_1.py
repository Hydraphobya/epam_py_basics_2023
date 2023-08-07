import random

# generate list of 100 random values from 0 to 1000
x = random.sample(range(0, 1000), 100)
number_of_permutations = 1
while number_of_permutations > 0:
    number_of_permutations = 0
    i = 0
    while i < 99:
        if x[i] > x[i + 1]:
            save_point = x[i]
            x[i] = x[i + 1]
            x[i + 1] = save_point
            number_of_permutations += 1
        i += 1
odd_counter = 0
odd_summ = 0
even_counter = 0
even_summ = 0
for num in x:
    if num % 2 == 1:
        even_counter += 1
        even_summ += num
    else:
        odd_counter += 1
        odd_summ += num
print(even_summ / even_counter)
print(odd_summ / odd_counter)
