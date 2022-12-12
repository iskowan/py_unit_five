'''
for x in range(6):
    print(x)
'''
'''
x = 0
while x < 5:
    print(x)
    x = x + 1
'''
# good way to make sure the user is putting in the correct input
'''

while True:
    play_again = input("Would you like to play again? y/n : ")
    if play_again == "y" or play_again == "n":
        break
print("I am out of the loop")
'''
'''
import random
tries = 0
total = 0
while total != 12:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    tries += 1                      # same things as tries = tries + 1
    total = die1 + die2
print("It took", tries, "tries to get a 12")
'''
