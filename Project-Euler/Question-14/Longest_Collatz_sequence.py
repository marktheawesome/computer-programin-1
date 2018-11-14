'''


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time 
start = time.time()
start_number = 0 
length = 0 
length_of_previous_sequence = 0 
longer_tree_number = 0 
def collatz_formula(n):
    l = 0 
    while n > 1:
        if n % 2 == 0:
            n = n/2 
            l+=1
        else:
            n = n * 3 +1 
            l +=1
    return l 

for start_number in range(1000000):
    length = collatz_formula(start_number)
    if length > length_of_previous_sequence:
        length_of_previous_sequence = length
        longer_tree_number = start_number
        print(length,start_number)

elapsed = time.time() - start

print(longer_tree_number, elapsed)
