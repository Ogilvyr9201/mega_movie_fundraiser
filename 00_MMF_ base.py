# functions go here


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


# Number checker that checks users input for any scenario From last years code
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
                    continue

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



# *** main routine ***
max_tickets = 5

name = ""
ticket_count = 0
ticket_sales = 0
max_tickets = 5

# loop code where it asks user for details
while name != "xxx"  and ticket_count < max_tickets:

    # ask user for name 
    name = not_blank("Name: ", "<error> please enter your name")

    if name == "xxx":
        print()
        break

    # asks user for age
    age = num_check("Age: ", "<error> please enter age.", int , None, -1)
    
    # checks if users age is between the perameters 
    if age < 12:
        print("Only those who are above 12 years old can purchase a ticket \n"
        "Sorry for the inconvenience.")
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
    
    # totals the ticket sales
    ticket_sales += ticket_price

    print("Ticket Price: ${:.2f} ".format(ticket_price))

    # calculate tickets left
    ticket_count += 1
    tickets_left = max_tickets - ticket_count
    # checks if there is only 1 space left
    if tickets_left == 1:
        print("THERE IS ONE SPACE LEFT!")
    else:
        print("You have {} seats left".format(tickets_left))
    print()

# figures out profit out side of loop
tiket_profit = ticket_sales - (5 * ticket_count)

# Print results of loop
# if youve sold put it prints that
if tickets_left == 0:
    print("You have sold out")

# if you have not sold out it tells you how many sold and left
else:
    print("You sold {} tickets.".format(ticket_count))
    print("{} spaces remain.".format(tickets_left))
print()

# shos profit made 
print("Profit: {:.2f}".format(tiket_profit))

