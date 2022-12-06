import random
def get_number():
    random.randint(1, 100)

def guess(number):
    guess = int(input("What number do you think I am thinking about?: "))
    count = 0
    while True:
        if guess > number:
            print("Your guess is greater than the number I am thinking about, try again!")
            count += 1
        if guess < number:
            print("Your guess is less than the number I am thinking about, try again!")
            count += 1
        if guess == number:
            break
    return count
def main():
    number = get_number()
    guess(number)

    print("You took", guess(number),"tries")
main()