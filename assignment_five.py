import random
import time
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def get_number():
    print("Getting number", end = '')
    time.sleep(1)
    print(".", end = '')
    time.sleep(1)
    print(".", end = '')
    time.sleep(1)
    print(".")
    number = random.randint(1, 100)
    time.sleep(1)
    print("Ok! I am thinking about a number")
    time.sleep(1)
    return number
def guess():
    number = get_number()
    guess = int(input("What number do you think I am thinking about?: "))
    count = 1
    while True:
        if guess > number:
            print("Your guess is", color.BOLD + color.GREEN + "greater" + color.END, "than the number I am thinking about, try again!")
            count += 1
            guess  = int(input("What number do you think I am thinking about?: "))
        if guess < number:
            print("Your guess is", color.BOLD + color.RED + "less" + color.END,"than the number I am thinking about, try again!")
            count += 1
            guess = int(input("What number do you think I am thinking about?: "))
        if guess == number:
            print("You guessed the number I was thinking about!")
            time.sleep(2)
            print("My number was:", color.BOLD + str(number) + color.END)
            time.sleep(2)
            return count

def main():
    print("Welcome!")
    time.sleep(1)
    print("This is a guessing game where I think of a number between 1 and 100")
    time.sleep(2)
    print("There are 3 rounds in this game...")
    time.sleep(1)
    print("Then I will give you the average amount of tries to took you to guess my number")
    time.sleep(1)
    print("You took", color.BOLD + str(guess()) + color.END,"tries to guess my number")
    time.sleep(1)
    print("Let's try again...")
    time.sleep(2)
    print("You took", color.BOLD + str(guess()) + color.END, "tries to guess my number")
    time.sleep(1)
    print("End of round 2")
    time.sleep(2)
    print("You took", color.BOLD + str(guess()) + color.END, "tries to guess my number")
main()