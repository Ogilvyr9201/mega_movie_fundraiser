# checks if string is valid returned in title case
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
        

# Checks that users input is not blank and returns name once input corretcly
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if not response:
            print(error)
        elif str.isspace(response):
            print(error)
        else:
            return response



pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]


# loop code where it asks user for details
name = ""
while name != "xxx":

    # ask user for name 
    name = not_blank("Name: ", "<error> please enter your name")

    if name == "xxx":
        print()
        break

    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit): ").lower()
        how_pay = string_checker(how_pay, "<error> please input correct payment method.", pay_method)

    # ask for subtotal
    subtotal = float(input("Subtotal: $"))

    # do maths to figure our surcharge
    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    
    else:
        surcharge = 0

    total = subtotal + surcharge

    # print users info
    print("Name: {}  |  Subtotal:  ${:.2f}  |  Surcharge:  ${:.2f}  |  Total Pay:  ${:.2f}"
    .format(name, subtotal, surcharge, total))
