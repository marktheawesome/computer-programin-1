fizz = 3 
buzz = 5

for num in range(100):
    if num % fizz == 0 and num % buzz == 0:
        print("fizzbuzz")
    elif num % fizz == 0:
        print("fizz")
    elif num% buzz == 0:
        print("buzz")
    else:
        print(num)