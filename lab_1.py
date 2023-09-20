import random

# generate list of 100 random values from 0 to 1000
x = random.sample(range(0, 1000), 100)
# declare counter for the number of permutations
number_of_permutations = 1
# bubble sort
# do until there will be no changes in the list
while number_of_permutations > 0:
    number_of_permutations = 0
    i = 0
    # we are going through the whole list. Instead of fixed number can be used len(x) function
    while i < 99:
        # if left valuer bigger than the right one do exchange
        if x[i] > x[i + 1]:
            save_point = x[i]
            x[i] = x[i + 1]
            x[i + 1] = save_point
            # increase changes counter
            number_of_permutations += 1
        # moving to the next item
        i += 1
# calculation of the average for the odd and even numbers
odd_counter = 0
odd_summ = 0
even_counter = 0
even_summ = 0
for num in x:
    if num % 2 == 0:
        even_counter += 1
        even_summ += num
    else:
        odd_counter += 1
        odd_summ += num
try:
    print('Even numbers average: ', even_summ / even_counter)
except ZeroDivisionError:
    print('There is no even numbers in the list!')
try:
    print('Odd numbers average: ', odd_summ / odd_counter)
except ZeroDivisionError:
    print('There is no odd numbers in the list!')
print('Sorted array: ', x)

"""
# ---- Another solution ----
total_sum = sum(random_numbers)
total_count = len(random_numbers) 

odd_list = [elem for elem in random_numbers if elem % 2]
odd_sum = sum(odd_list)
odd_count = len(odd_list) 

even_sum = total_sum - odd_sum
even_count = total_count - odd_count
even_avg = even_sum / even_count if even_count else 0 # or None
"""
