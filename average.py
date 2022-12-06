tries = 1
while True:
    q = input("please press a random letter: ")                     # get input from user
    if q != "q":                                                    # if the user does not press q then:
        tries += 1                                                  # add one to a varible called "tries"
        print("You did not press the right key")                    # tells the user that they didnt click the right key... repeat
    if q == "q":                                                    # when the user click the right key:
        print("it took", tries, "tries to press the \"q\" key")     # tell them how many tries it too them
        break                                                       # end the loop by breaking it