import random

def get_stones():
    random.randint(1, 10)

def get_row1():
    row1 = get_stones()
    return row1

def get_row2():
    row2 = get_stones()
    return row2

def get_winner():
    pass
def main():
    print("There are two rows, row one has", get_row1(), "stones in it and row two has", get_row2(), "stones in it.")
    pile = input("Which pile would you like to choose from?:")
    amount = input("How many stones would you like to remove?:")

main()