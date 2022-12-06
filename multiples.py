'''
def get_sum(number):
    num = 0
    for x in range(number):
        running_num = num + 1
        if running_num % 3 == 0:
            num_1 = running_num
        if running_num % 5 == 0:
            num_2 = running_num
        num = running_num
    total = num_1 + num_2
    print("The mutiples of 3 and 5 total is", total )
get_sum(5)
'''

def get_sum(number):
    sum = 0
    for x in range(number):
        print("x is", x)
        if x % 3 == 0 or x % 5 == 0:
            print("...adding", x, "to total")
            sum += x
            print("Current total is: \033[1m", sum, "\033[0m")
    print("The sum of the multiples of 3 and 5 are", "\033[1m",sum, "\033[1m")

get_sum(10)
"""
    Will return the sum of all the multiples of 3 or 5 of the given number.
    Ex. get_sum(10) returns 23
    :param number: The value up to which we want to find the sum. Not included in the calculation
    :return: The sum of all the multiples of 3 or 5 up to the number.
"""
#pass # make sure to delete this line when writing your function