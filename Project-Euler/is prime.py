num = input("give me a number:")
num = int(num)


def prime_check(num):
    n = num - 1

    while n > 1:

        if num % n == 0 and n >= 1 :
            return False
        n = n-1 

    return True

is_prime = prime_check(num)

if is_prime:
    print("It is prime")
else:
    print("It is not prime.")