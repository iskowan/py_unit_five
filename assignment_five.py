import random               # importing random for a random number
import time                 # importing time for pausing time
class color:                # creating a class called color
   GREEN = '\033[92m'       # defining GREEN
   RED = '\033[91m'         # defining RED
   BOLD = '\033[1m'         # defining BOLD
   UNDERLINE = '\033[4m'    # defining UNDERLINE
   END = '\033[0m'          # defining END
def get_number():
    '''
    this function gets numbers and outputs them back for the user to guess
    :return: number returns the number that was randomly picked using random
    '''
    print("Getting number", end='')                     # prints text and places the next line of text next to it
    time.sleep(1)                                       # pauses the code for 1 second
    print(".", end='')                                  # prints "." and places the next line of text next to it
    time.sleep(1)                                       # pauses the code for 1 second
    print(".", end='')                                  # prints "." and places the next line of text next to it
    time.sleep(1)                                       # pauses the code for 1 second
    print(".")                                          # prints "."
    number = random.randint(1, 100)                     # get a random number between 1 and 100
    time.sleep(1)                                       # pauses the code for 1 second
    print("Ok! I am thinking about a number")           # prints text
    time.sleep(1)                                       # pauses the code for 1 second
    return number                                       # returns the number chosen in line 26 for another function to use
def guess():
    '''
    this function gets the user guesses and lets them know if they are too high or low
    :return: count returns the tries that it took for the user to guess the number
    '''
    number = get_number()                                                                                                                   # calls the function "get_number()"
    guess = int(input("What number do you think I am thinking about?: "))                                                                   # gets input of the user for their guess
    count = 1                                                                                                                               # counts the tries that the user takes (counter is 1)
    while True:
        if guess > number:                                                                                                                  # if the users guess is greater than the number
            print("Your guess is", color.BOLD + color.GREEN + "greater" + color.END, "than the number I am thinking about, try again!")     # print the text
            count += 1                                                                                                                      # add one to the counter
            guess  = int(input("What number do you think I am thinking about?: "))                                                          # ask the user for another guess (input)
        if guess < number:                                                                                                                  # if the guess is less than the number
            print("Your guess is", color.BOLD + color.RED + "less" + color.END,"than the number I am thinking about, try again!")           # print the text
            count += 1                                                                                                                      # add one to the counter
            guess = int(input("What number do you think I am thinking about?: "))                                                           # ask the user for another guess (input)
        if guess == number:                                                                                                                 # if the guess is the same as the number
            print("You guessed the number I was thinking about!")                                                                           # print text
            time.sleep(2)                                                                                                                   # pauses time for 2 seconds
            print("My number was:", color.BOLD + str(number) + color.END)
            time.sleep(2)                                                                                                                   # pauses time for 2 seconds
            return count

def main():
    print("Welcome!")
    time.sleep(1)                                                                               # pauses time for 1 seconds
    print("This is a guessing game where I think of a number between 1 and 100")                # print text
    time.sleep(2)                                                                               # pauses time for 2 seconds
    print("There are 3 rounds in this game", end='')                                            # print text amd places the next line of text next to it
    time.sleep(.5)                                                                              # pauses time for .5 seconds
    print(".", end='')                                                                          # prints "." and places the next line of text next to it
    time.sleep(.5)                                                                              # pauses the code for .5 second
    print(".", end='')                                                                          # prints "." and places the next line of text next to it
    time.sleep(.5)                                                                              # pauses the code for .5 second
    print(".")                                                                                  # prints "."
    time.sleep(2)                                                                               # pauses time for 1 second
    print("Then I will give you the average amount of tries to took you to guess my number")    #print text
    time.sleep(2)                                                                               # pauses time for 1 seconds
    print("You took", color.BOLD + str(guess()) + color.END,"tries to guess my number")         # print text and call guess fucntion
    time.sleep(1)                                                                               # pauses time for 1 seconds
    print("Let's try again...")                                                                 # print text
    time.sleep(2)                                                                               # pauses time for 2 seconds
    print("You took", color.BOLD + str(guess()) + color.END, "tries to guess my number")        # print text and call guess fucntion
    time.sleep(1)                                                                               # pauses time for 1 seconds
    print("End of round 2")                                                                     # print text
    time.sleep(2)                                                                               # pauses time for 2 seconds
    print("You took", color.BOLD + str(guess()) + color.END, "tries to guess my number")        # print text and call guess function
    print("Thanks for playing!")                                                                # print text
    time.sleep(1)                                                                               # pauses time for 1 second
    print("See you later!")                                                                     # print text
main()                                                                                          # calls main function