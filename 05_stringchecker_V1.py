# functions


def string_checker(question, error, to_check):
    valid = False
    while not valid:
        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                #checks if response is the first letter of an item in the list
                if response == item[0]:
                    # note: returns the entire response
                    #rather then first letter
                    return item
                
        print(error)


# main routine
# asks user if they want snacks 
while 1 == 1:
    want_snacks = string_checker("Would you like to order snacks? ",
    "<error> plaease sya yes/y or no/n.", ["yes", "no"])
    print("Answer: {}".format(want_snacks))
    print()