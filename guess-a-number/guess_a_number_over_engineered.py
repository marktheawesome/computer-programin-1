'''
9/6/2018 11:04
    The game will be between 2 randomely selected paramters.
    next make it cap the number of trys
'''

'''
9/6/2018 11:19
    the game now keeps track of number og guesses and limits it to 5
'''

'''

'''

def game():
    import random

    #variables 
    random = random.randint 
    low = random(0,1000)
    high = random(0,1000)
    tries = 1

    #helper functions
    while low > high:
        low = random(0,1000)
        high = random(0,1000)
        
    def get_guess ():
        while True:
            num = input('take a guess:')

            if num.isnumeric() and low<=int(num)<= high:
                num = int(num)
                return num
            else:
                print("Invalid guess Pleases enter a number.")

    #game play
    rand = random(low,high)
    print ("I'm think of a number between " + str(low) + " and " + str(high) + ".")

    got_it = False
    limit = random(5,15)
    print("number of tries, " + str(limit))

    while got_it == False and tries <= limit:
        guess = get_guess()
        tries = tries + 1 
        if guess == rand:
            got_it = True
        elif guess > rand:
            print ('you guessed too high.')
        elif guess < rand:
            print('you guessed too low')

    if got_it == True:
        print ("you won!")
    else:
        print ("You lost ;(")

game()