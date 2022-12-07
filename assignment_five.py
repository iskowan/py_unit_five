# Anderson Iskowitz
# 12/7/2022
# this is a guessing game for Unit 5 final project
import random                       # importing random for a random number
import time                         # importing time for pausing time
import sys                          # importing sys for scrollTxt
def scrollTxt(text):                # https://replit.com/talk/ask/How-do-we-print-letters-by-letters-in-python/34360
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
def get_number():
    '''
    this function gets numbers and outputs them back for the user to guess
    :return: number returns the number that was randomly picked using random
    '''
    scrollTxt("Getting number")                         # prints text and places the next line of text next to it
    time.sleep(.8)                                      # pauses the code for 1 second
    print(".", end='')                                  # prints "." and places the next line of text next to it
    time.sleep(.8)                                      # pauses the code for 1 second
    print(".", end='')                                  # prints "." and places the next line of text next to it
    time.sleep(.8)                                      # pauses the code for 1 second
    print(".")                                          # prints "."
    number = random.randint(1, 100)                     # get a random number between 1 and 100
    time.sleep(1)                                       # pauses the code for 1 second
    scrollTxt("Ok! I am thinking about a number\n")     # prints text
    time.sleep(1)                                       # pauses the code for 1 second
    return number                                       # returns the number chosen in line 26 for another function to use
def guess():
    '''
    this function gets the user guesses and lets them know if they are too high or low
    :return: count returns the tries that it took for the user to guess the number
    '''
    number = get_number()                                                                                                   # calls the function "get_number()"
    scrollTxt("What number do you think I am thinking about?:")                                                             # gets input of the user for their guess
    guess = int(input(" "))                                                                                                 # gets input for printed question
    count = 1                                                                                                               # counts the tries that the user takes (counter is 1)
    while True:                                                                                                             # loops until it is broken
        if guess > number:                                                                                                  # if the users guess is greater than the number
            scrollTxt("Your guess is\033[92m\033[1m greater\033[0m than the number I am thinking about, try again!\n")      # print the text
            count += 1                                                                                                      # add one to the counter
            scrollTxt("What number do you think I am thinking about?:")                                                     # print the text
            guess = int(input(" "))                                                                                         # gets input for the printed question
        if guess < number:                                                                                                  # if the guess is less than the number
            scrollTxt("Your guess is\033[91m\033[1m less\033[0m than the number I am thinking about, try again!\n")         # print the text
            count += 1                                                                                                      # add one to the counter
            scrollTxt("What number do you think I am thinking about?:")                                                     # print the text
            guess = int(input(" "))                                                                                         # gets the input for the printed question
        if guess == number:                                                                                                 # if the guess is the same as the number
            scrollTxt("You guessed the number I was thinking about!\n")                                                     # print text
            time.sleep(2)                                                                                                   # pauses time for 2 seconds
            scrollTxt("My number was: \033[1m" + str(number) + "\033[0m\n")                                                 # prints what the number was
            time.sleep(2)                                                                                                   # pauses time for 2 seconds
            return count                                                                                                    # returns the counter
def average(num1, num2, num3):                  # defining varible "average"
    '''
    this calculates the average of the amount of times it took the user to guess
    :param num1: this is the counter after the first round
    :param num2: this is the counter after the second round
    :param num3: this is the counter after the third round
    :return: returns the total after calculating the average
    '''
    total = num1 + num2 + num3                  # adding the three counter totals together
    new_total = round((total/3), 0)             # dividing the total of the three counters by three and rounding it to the 0 decimal
    return new_total                            # returning the new total
def main():
    scrollTxt("Welcome!\n")
    time.sleep(1)                                                                                       # pauses time for 1 seconds
    scrollTxt("This is a guessing game where I think of a number between 1 and 100\n")                  # print text
    time.sleep(1)                                                                                       # pauses time for 2 seconds
    scrollTxt("There are 3 rounds in this game")                                                        # print text amd places the next line of text next to it
    time.sleep(1)                                                                                       # pauses time for .5 seconds
    print(".", end='')                                                                                  # prints "." and places the next line of text next to it
    time.sleep(1)                                                                                       # pauses the code for .5 second
    print(".", end='')                                                                                  # prints "." and places the next line of text next to it
    time.sleep(1)                                                                                       # pauses the code for .5 second
    print(".")                                                                                          # prints "."
    time.sleep(1)                                                                                       # pauses time for 1 second
    scrollTxt("Then I will give you the average amount of tries to took you to guess my number\n")      #print text
    time.sleep(1)                                                                                       # pauses time for 1 seconds
    while True:
        guess1 = guess()                                                                                # naming the function as guess1 to calcualte the average conter
        scrollTxt("You took \033[1m" + str(guess1) + "\033[0m tries to guess my number\n")              # print text and call guess fucntion
        time.sleep(1)                                                                                   # pauses time for 1 seconds
        scrollTxt("Let's try again...\n")                                                               # print text
        time.sleep(1)                                                                                   # pauses time for 2 seconds
        guess2 = guess()                                                                                # naming the function as guess2 to calculate the average counter
        scrollTxt("You took \033[1m" + str(guess2) + "\033[0m tries to guess my number\n")              # print text and call guess fucntion
        time.sleep(1)                                                                                   # pauses time for 1 seconds
        scrollTxt("End of round 2\n")                                                                   # print text
        time.sleep(1)                                                                                   # pauses time for 2 seconds
        guess3 = guess()                                                                                #naming the function as guess3 to calcualte the average counter
        scrollTxt("You took \033[1m" + str(guess3) + "\033[0m tries to guess my number\n")              # print text and call guess function
        print("The average amount of tries it took you was", average(guess1, guess2, guess3))           # printing the average amount of guesses it took the user
        scrollTxt("Thanks for playing!\n")                                                              # print text
        time.sleep(1)                                                                                   # pauses time for 1 second
        scrollTxt("See you later!\n")                                                                   # print text
main()                                                                                                  # calls main function