def get_sum(num):
    test = ""
    for x in range(1, 13):
         test += str(x * num) + " "
    print(test)

def main():
    for x in range(1, 13):
        get_sum(x)
        '''
        num = int(input("What times table would you like to see?:"))
        get_sum(num)
        '''

main()

"""
    Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
    :param number: An integer
    :return: A string of 12 values representing the mulitiplication table of the parameter number.
    """
pass # Make sure to delete this line when writing your function.