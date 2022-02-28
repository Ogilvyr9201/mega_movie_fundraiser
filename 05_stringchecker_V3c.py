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
# errors list

snack_error = "<error> Please enter 1 of the 4 snack options."
yes_no_error ="<error> please enter yes or no."


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
            if desired_snack == "xxx":
                break
            else:
                snack_order.append(desired_snack)

            # checks if response is asking for multiple
            print("Chosen snack: {}".format(desired_snack))

print()
for item in snack_order:
    print(snack_order)