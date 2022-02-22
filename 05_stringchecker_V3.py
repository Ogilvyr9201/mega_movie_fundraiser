# functions


def string_checker(question, error, options):

    response = input(question)
    
    for var_list in options:

        # if the snack is in one of the lists
        if response in var_list:

            # Get full name of snack and put it 
            # in title case so it looks nice
            response = var_list[0].title()
            is_valid = "yes"
            break
        
        else:
            is_valid = "no"

    if is_valid == "yes":
        return response
    
    else:
        print(error)



# main routine
# errors list
error_list = [
    "<error> Please enter 1 of the 4 snack options.",
    "<error> please enter yes or no."
]

# a list of all the snacks and valid responses to order snacks
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# yes no list
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]

# initialize variables
snack_ok = ""
snack = ""
 
# asks user if they want snacks 
for item in range(0, 6):

    # ask user if they want snacks
    want_snacks = string_checker("Would you like snacks? ", error_list[1], yes_no_list)
    
    if want_snacks == "Yes":
        # asks user what snack they want
        desired_snack = string_checker("Snack: ", error_list[0], valid_snacks)
        print("Chosen snack: {}".format(desired_snack))
    