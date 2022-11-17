# 1, 1, 2, 3, 5, 8, 13, etc.
def fibonacci(num):
    a = 1
    b = 1
    num_list = "1 1 "
    for x in range(num):
        c = a + b
        num_list += str(c) + " "
        a = b
        b = c
    print(num_list)
fibonacci(19)

"""
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
