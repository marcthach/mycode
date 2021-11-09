#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""

round = 0           # integer round initiated to 0
answer=""

while round < 3 and answer != "brian":
    round = round + 1     # increase the round counter
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______"\nYour guess--> ').lower()    # string ans collected from user
    if answer == 'brian': # logic to check if user gave correct answer
        print('Correct!')
        break             # break statement escapes the while loop
    elif answer == 'shrubbery': # logic to check if user gave correct answer
        print('You gave the super secret answer!')
        break             # break statement escapes the while loop
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was Brian.')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')

