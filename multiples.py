def get_sum(y):
    test = ""
    for x in range(1, 13):
        test += str(y * x) + " "
    print(test)

def main():
    num = int(input("What times table would you like to see?:"))
    get_sum(num)

main()

"""
    Will return the sum of all the multiples of 3 or 5 of the given number.
    Ex. get_sum(10) returns 23
    :param number: The value up to which we want to find the sum. Not included in the calculation
    :return: The sum of all the multiples of 3 or 5 up to the number.
"""
#pass # make sure to delete this line when writing your function