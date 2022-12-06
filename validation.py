'''
def get_input():
    user_input = int(input("Choose a number between 1 and 10: "))
    for x in range(int(user_input)):
        print(user_input)
        user_input += 1
    while True:
        if user_input != 1:
            return user_input
'''
def get_input():
    """
    This function ensures that a user correctly enters a number and not a string in the proper range.
    :return: a value between 1 and 10, inclusive
    """
    while True:
        try:
            userInput = int(input("Please enter a number between 1 and 10: "))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            if userInput >= 1 and userInput <= 10:
                return userInput
    """
    This function ensures that a user correctly enters in a number in the proper range.
    :return: a value between 1 and 10, inclusive
    """
    pass  # make sure to delete this line after you complete your function


def main():
    print(get_input())


if __name__ == '__main__':
    main()
