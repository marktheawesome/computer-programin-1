# number_1 = 3
# number_2 = 5 
current_number = 1
total = 0
upper_number = 1000

def meat(current_number,total,upper_number):
    while current_number < upper_number:
        if current_number % 3 == 0 or current_number % 5 == 0:
            total = total + current_number
            
        current_number = current_number +  1

    return total

#main

total = meat(current_number,total,upper_number)
print(total)
