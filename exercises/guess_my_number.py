"""Works as follows: 
You (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number.
"""

high = 100
low = 0
mid = high // 2

print("Please think of a number between 0 and 100!")

while True:
    feedback = input("Is your secret number " + str(mid) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if feedback == 'h':
        high = mid
        mid = (low + high) // 2
    elif feedback == 'l':
        low = mid
        mid = (low + high) // 2
    elif feedback == 'c':
        print("Game over. Your secret number was: " + str(mid))
        break
    else:
        print("Sorry, I did not understand your input.")