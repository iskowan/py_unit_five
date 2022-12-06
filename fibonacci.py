# 1, 1, 2, 3, 5, 8, 13, etc.
def fibonacci(num):                     # defining the function "fibonacci" with a varible called "num"
    a = 1                               # definging "a" = 1
    b = 1                               # defining "b" = 1
    num_list = "1 1 "                   # defining a varible named "num_list" as equal to "1 1"
    for x in range(num - 2):            # creating loop that repeates two times less than "num"
        c = a + b                       # defining c as a + b (first time around c = 2)
        num_list += str(c) + " "        # adding c to the varible "num_list"
        a = b                           # defining "a" as "b" now
        b = c                           # defining "b" as "c" now
                                        # (first time around now: a = 1 and b = 2)
    print(num_list)                     # the varible "num_list" is printes for the viewer to see
fibonacci(5)                            #finally the function is called

"""
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
