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
# a list of all the snacks and valid responses to order snacks
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# initialize variables
snack_ok = ""
snack = ""
 
# asks user if they want snacks 
for item in range(0, 3):
    # asks user what snack they want
    desired_snack = input("Snack: ")

    for var_list in valid_snacks:

        # if the snack is in one of the lists
        if desired_snack in var_list:
            # Get full name of snack and put it 
            # in title case so it looks nice
            snack = var_list[0].title()
            snack_ok = "yes"

    if snack_ok == "yes":
        print("Snack Choice: {}".format(snack))
    
    else:
        print("Invalid Choice")
