from itertools import combinations

""" 
This module provides the solutions for part 1 and part 2 of the problems found here https://adventofcode.com/2017/day/2
"""

# part one

# covert input to list format
input = open("input.txt", "r")

list_of_lists = []

for line in input:

  stripped_line = line.strip()

  line_list = sorted(list(map(int, stripped_line.split())), reverse=True)

  list_of_lists.append(line_list)

input.close()

check_sum = 0

# iterate through each row and find the largest and smallest number, then find the difference between the two numbers
for row in list_of_lists:
    check_sum += max(row) - min(row)

print(f'The checksum is {check_sum}')

# part 2

divisible_sum = 0
combinations_list = []

# find all possible combinations in the given lists
# https://docs.python.org/3/library/itertools.html#itertools.combinations
for a_list in list_of_lists:
    combinations_list.append(list(combinations(a_list, 2)))

# iterate through the combinations and find the evenly divisible combinations
# if any evenly divisible combinations are found, add the quotient to the final result
for combination in combinations_list:
    for combo in combination:
        if combo[0] % combo[1] == 0:
            divisible_sum += combo[0] / combo[1]

print(f'The divisible sum is {divisible_sum}')



