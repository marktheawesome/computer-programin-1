import time

print("ready to playt Mad Libs?")
time.sleep(1)
print ('If you are readay press the Enter key')

input()

print(' Give me an adjective, plese ')
adjective = input()

print(' Now a noun ')
noun = input()

print(' I need a plural_noun. ')
plural_noun = input()

print(' How about a female in the room. ')
person_in_the_room_female = input()

print(' I need another adjective. ')
adjective_2 = input()

print(' Article of clothing? ')
article_of_clothing = input()

print(' A secound noun. ')
noun_2 = input()

print(' A city plese. ')
a_city = input()

print(' Another plural noun. ')
plural_noun_2 = input()

print(' Give me an adjective, plese ')
adjective_6 = input() 

print(' Part of the body, plese. ')
part_of_the_body = input()

print(' Pick a letter fo the alphabet. ')
letter_of_the_alphabet = input()

print(' Name a clebrity. ')
celebrity = input()

print(' Plural noun, plese. ')
plural_noun_3 = input()

print(' One last adjective!!! ')
adjective_3 = input()

print(' What is your favorit place? ')
a_place = input()
 
print(" We're getting close. i can see it coming together. ")

time.sleep(3)

print(" Another part of the body ")
part_of_the_body_2 = input()

print(' I lied. More adjectives!!!!!!!!! ')
adjective_4 = input()

print('Honestly last adjective.')
adjective_5 = input()

print(' verb? ')
verb =  input()

print(' Plural noun. ')
plural_noun_4 = input()

print(' Last I need a number. ')
number = input()

#print(' there are many ')  
#+ adjective +
#' ways to choose a '
#+ noun + 
#'to read. First, you could ask for recommendations from you friends and '
#+ plural_noun +
#". Just don't ask Aunt"
#+ person_in_the_room_female +
#" - She only reads "
#+ adjective_2 +
#' books with '
#+ article_of_clothing +
#'-ripping goddesses on the cover. If your friends and family are no help, try checking out the '
#+ noun_2 +  
#"Review in the "
#+ a_city +
#"times. if the "
#+plural_noun_2 +
#"featured there are too "
#+ adjective_6 +
#"for your taste, try something a little more low-"
#+ part_of_the_body +
#", like "
#+ letter_of_the_alphabet +
#': The'
#+ celebrity +
#'magazing, or'
#+ plural_noun_3 +
#'Magazie. You could aslo choose a book the '
#+ adjective_3 +
#'-fashioned way. Head to your local libary or '
#+ a_place +
#"and bowse the shelves until something catches your "
#+ part_of_the_body_2 +
#  ". Or, you could save yourdelf a whole lot of "
#  + adjective_4 +
#  'trouble and log on to www.bookish.com, the '
#  + adjective_5 +
#  'new website to '
#  + verb +
#  "for books! With all the time you'll sve not having to search for "
#  + plural_noun_4 +
# ",you can read "
#  + number+
# "more books!"

time.sleep(1.2)

print('I will need some time to put this together.')
time.sleep(5)

print('There are many ' + adjective + ' ways to choose a ' + noun + ' to read.')
print("First, you could ask for recommendations from you friends and " + plural_noun + ".")
print("Just don't ask Aunt " + person_in_the_room_female + " - She only reads " + adjective_2 + ' books with ' + article_of_clothing + '-ripping goddesses on the cover.')
print('If your friends and family are no help, try checking out the ' + noun_2 + " review in the " + a_city + " times.")
print('If the ' + plural_noun_2 + " featured there are too " + adjective_6 + " for your taste, try something a little more low- " + part_of_the_body + ", like " + letter_of_the_alphabet + ': The ' + celebrity + ' magazing, or ' + plural_noun_3 + ' Magazie. ')
print('You could aslo choose a book the ' + adjective_3 + '-fashioned way.')
print('Head to your local libary or ' + a_place + " and bowse the shelves until something catches your " + part_of_the_body_2 + '.')
print("Or, you could save yourdelf a whole lot of " + adjective_4 + 'trouble and log on to www.bookish.com, the ' + adjective_5 + 'new website to ' + verb + "for books!")
print("With all the time you'll sve not having to search for " + plural_noun_4 + ",you can read " + number+ " more books!")



time.sleep(30)
print("Did you like the game? On a scale of 1-5 five being the best what would you give?")
rating = input()

if rating == '5':
    print("Glade you really enjoyed it. Thank you!")
elif rating =='4' :
    print ("Glade you enjoyed it. Thank you for playing!")
elif rating == '3':
    print("Thank you for playing, good luck with your project.")
elif rating == '2':
    print("thank you for your honesty. I'll do better next time")
elif rating =='1': 
    print("I didnt think it was that bad. You are just jealous.")
else:
    print ("you can't follow simple directions. pick a number 1,2,3,4,5. That's it.I don't even trust you DON'T try agian!")
