#Anderson Iskowitz
def count(first, last, step):
    test = ""
    for x in range(first, last, step):
        test += str(x)+ " "
    print(test)

"""
    This function will create a string of numbers separated by a space. The numbers will start with the
    first number and end with the second. The second number SHOULD be included as part of the string. If
    the first number is larger than the second, the numbers should count down, rather than up.
    count(5, 10) returns "5 6 7 8 9 10 "
    :param first: The starting number
    :param second: The final number. Must be included
    :return: A string containing the numbers
    """

def main():
    (count(6, -1, -1))


if __name__ == '__main__':
    main()

