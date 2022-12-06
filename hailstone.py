def sequence(number):
    """
    If the number n is odd - 3*n + 1
    If the number n is even n / 2
    :param number: The starting number for the Hailstone sequence
    :return: The number of steps taken to reach 1
    """
    counter = 0
    while True:
        if number % 2 == 0:                 # if number divided by 2 has a remainder of zero, do the following:
            number = number/2               # divide number by 2 and remake number as the answer
            counter += 1                    # add one to the counter
            if number == 1:                 # if the remainder equals one...
                return counter              # return the total of counter
        if number % 2 != 0:                 # if the number divided by 2 does not equal zero, do the following:
            number = number * 3 + 1         # mulitply the number by 3 and add one; remake the varible to the total of this
            counter += 1                    # add one to the counter
            if number == 1:                 # if the number total is 1
                return counter              # return the total counter

def main():                                                     # defining the main function
    num = int(input("What number would you like to try?: "))    # ask the user what number they would like to input
    print("it took",sequence(num),"steps to reach 1")           # call the function and print the total within a string

main()                                                          # call main