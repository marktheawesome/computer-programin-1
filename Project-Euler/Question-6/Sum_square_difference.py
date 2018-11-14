n = 0 
sum_of_the_squares_total = 0
import time 
start = time.time()

def sum_of_the_squares(n):
    sum_of_the_squares_total = 0 
    while n <= 100:
        sum_of_the_squares_total = sum_of_the_squares_total + (n**2)
        n += 1
    return sum_of_the_squares_total

def square_of_the_sum_of(n):
    total = 0 
    while n <= 100:
        total = total + n 
        n += 1
    total = (total**2)
    return total 


sum_of_the_squares_total = sum_of_the_squares(n)

square_of_the_sum_of_total = square_of_the_sum_of(n)

difference = square_of_the_sum_of_total - sum_of_the_squares_total
elapsed = time.time() - start
print(difference,elapsed)