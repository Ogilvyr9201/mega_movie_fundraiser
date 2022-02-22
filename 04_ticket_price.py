# main routine
# Functions go here


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, exit_code=None, low=None, high=None):

    valid = False
    while not valid:
        try:
            # Checks if user inputs exit code
            response = input(question)
            if response == exit_code:
                return response
            else:
                response = num_type(response)
            
            # Checks if they inputed correct number
            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    return 

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()



# main routine
profit = 0
# ask user for there age

while 1 == 1:
    age = num_check("Age: ", "<error> please enter age.", int, None, -1)
    
    # checks if users age is between the perameters 
    if age < 12:
        print("Only those who are above 12 years old can purchase a ticket \n"
        "Sorry for your inconvenience.")
        print()
        continue
    elif age > 130:
        print("Are you really that old??")
        print()
        continue

    # finds out ticket price 
    if age > 64:
        ticket_price = 6.5
    elif age < 16:
        ticket_price = 7.5
    else:
        ticket_price = 10.5

    # figures out profit 
    profit_made = ticket_price - 5
    profit += profit_made

    print("Ticket Price: ${:.2f} ".format(ticket_price))
    print()
    print("Profit: {:.2f}".format(profit))
