import re


# functions


def string_checker(question, error, options):

    response = input(question).lower()
    
    for var_list in options:

        # if the snack is in one of the lists
        if response in var_list:

            # Get full name of snack and put it 
            # in title case so it looks nice
            response = var_list[0].title()
            return response
        
    print(error)
        



# main routine
# regular expression to find if item starts with a number
number_regex = "^[1-9]"

# errors list
snack_error = "<error> Please enter 1 of the 4 snack options."
yes_no_error ="<error> please enter yes or no."


# a list of all the snacks and valid responses to order snacks
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["xxx"]
]

# yes no list
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]

# initialize variables
snack_ok = ""
snack = ""


# holds snack order for a single user.
snack_order = []
 

# ask user if they want snacks
check_snack = "invalid choice"
while check_snack == "invalid choice":
    check_snacks = string_checker("Do you want snacks?  ", yes_no_error, yes_no_list)

    if check_snacks == "Yes":

        desired_snack = ""
        while desired_snack != "xxx":
            
            # asks user what snack they want
            desired_snack = string_checker("Snack: ", snack_error, valid_snacks)

            # breaks loop is exit code used 
            if desired_snack == "Xxx":
                break
            elif desired_snack == None:
                print()
            else:
                snack_order.append(desired_snack)

            # checks if response is asking for multiple
            print("Chosen snack: {}".format(desired_snack))

        print()
        print("Snacks Ordered:")
        for item in snack_order:
            print(item)

    