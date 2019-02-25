import os 
def end_with_s(word_list):
    ''' how many words end with s? '''
    count = 0
    for word in word_list:
        if word[-1] == 's':
            count += 1

    return count

def two_letters(word_list):
    ''' how many words are 2 letters long? '''
    count = 0
    for word in word_list:
        if len(word) == 2:
            count += 1

    return count

def same_first_last(word_list):
    '''
    Returns a count of the number of words that have the same
    first and last letters
    '''

    number_of_words = 0 
    for word in word_list:
        if word[0] == word[-1]:
            number_of_words =number_of_words + 1
    return number_of_words

def number_of_letter(word_list, letter_list):
    '''
    Returns a count of occurences of letter in word list
    Hint: This requires two loops.
    '''
    letter = str(letter_list)
    number_of_letter = 0 
    # for letter in letter_list:
    for word in word_list:
        for char in word:
            if char == letter:
                number_of_letter +=1
    return number_of_letter


def sevens(word_list):
    '''
    Writes a new file called sevens.txt which contains only
    letters that are exactly seven letters long.
    '''
    number_of_sevens = 0 
    try:
        os.remove("all_seven_words.txt") 
    except:
        pass
    with open("all_seven_words.txt", "a") as f:
        for word in word_list:
            if len(word) == 7:
                f.write(word + "\n")
                number_of_sevens +=1
    return "go to file", number_of_sevens



# read a big file, don't try to print all items!
with open('scrabble_list.txt', 'r') as f:
    words = f.read().splitlines()

with open('letters.txt', 'r') as le:
    letter_list = le.read()

print(words[:10])
print(letter_list)

# call functions to answer questions
print( end_with_s(words) )
print( two_letters(words) )
print( same_first_last(words) )

for letter in letter_list:
    print( number_of_letter(words,letter), letter )

print(sevens(words))

print("done")