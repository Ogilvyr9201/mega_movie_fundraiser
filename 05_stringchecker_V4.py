import re


# functions


def string_checker(choice, error, options):


    for var_list in options:

        # if the snack is in one of the lists
        if choice in var_list:

            # Get full name of snack and put it 
            # in title case so it looks nice
            response = var_list[0].title()
            return response
            
    print(error)
    return "invalid choice"
        


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
    ["orange juice", "oj",  "o", "juice", "e"],
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
    want_snacks = input("Do you want snacks?  ").lower()
    check_snack = string_checker(want_snacks, yes_no_error, yes_no_list)

    if check_snack == "Yes":

        desired_snack = ""
        while desired_snack != "xxx":
            
            # asks user what snack they want
            desired_snack = input("Snack: ").lower()

            # breaks loop is exit code used 
            if desired_snack == "Xxx":
                check_snacks = "invalid choice"
                break

            # if item has a number separate it into two parts (number and item)
            if re.match(number_regex, desired_snack):
                amount= int(desired_snack[0])
                snack = (desired_snack[1:])

            # if item does not have a number infront, set number too 1
            else:
                amount = 1
                snack = desired_snack
            
            # remove white space around snack
            snack = snack.strip()
            
            # check if snack is valid
            snack_choice = string_checker(snack, snack_error, valid_snacks)

            # checks if amount is valid
            if amount >= 5:
                print("Sorry  - we have a four snack maximum")
                snack_choice = "invalid choice"

            # add snack and amount to list
            amount_snack = "{} {}.".format(amount, snack_choice)
            
            # append snack to list 
            if snack_choice != "xxx" and snack_choice != "invalid choice":
                snack_order.append(snack_choice)

        print()
        print("Snacks Ordered:")
        for item in snack_order:
            print(item)