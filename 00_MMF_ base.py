import re
import pandas
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


# checks if string is valid
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
        

# gets snacks
def get_snack():

    # holds snack order for a single user.
    snack_order = []

    # a list of all the snacks and valid responses to order snacks
    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&Ms","M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice", "oj",  "o", "juice", "e", "tenthplace"]
    ]

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []
        
        # asks user what snack they want
        desired_snack = input("Snack: ").lower()

        # breaks loop is exit code used 
        if desired_snack == "xxx":
            return snack_order

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
        snack_row.append(amount)
        snack_row.append(snack_choice)
        
        # append snack to list 
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


# checks if users age is valid
def ticket_check(tickets_sold, ticket_limit):

    # tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

    # if there is one seat left
    else:
        print("*** There is 1 Seat left ***")

    return    


# gets ticket price
def ticket_price():
    
    # asks user for age
    age = num_check("Age: ", "<error> please enter age.", int , None, -1)

    # checks if users age is between the perameters 
    if age < 12:
        print("Only those who are above 12 years old can purchase a ticket \n"
        "Sorry for the inconvenience.")
        return "invalid ticket price"

    elif age > 130:
        print("Are you really that old??")
        print()
        return "invalid ticket price"
    
    else:
        # finds out ticket price 
        if age > 64:
            ticket_price = 6.5
        elif age < 16:
            ticket_price = 7.5
        else:
            ticket_price = 10.5
        return ticket_price


# *** main routine ***
# regular expression to find if item starts with a number
number_regex = "^[1-9]"

# errors list
snack_error = "<error> Please enter 1 of the 4 snack options."
yes_no_error = "<error> please enter yes or no."

# yes no list
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]


# defines constants 
MAX_TICKETS = 5

# defines variables
name = ""
ticket_count = 0
ticket_sales = 0

# initialise lists (to make data-frame)
all_names = []
all_tickets = []

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]


# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Tickets': all_tickets,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Water': water,
    'Orange Juice': orange_juice
    
}

# price dictionary
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

# loop code where it asks user for details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # ask user for name 
    name = not_blank("Name: ", "<error> please enter your name")

    if name == "xxx":
        print()
        break

    # finds out ticket cost
    # and makes sure age is valid
    ticket_cost = ticket_price()
    if ticket_cost == "invalid ticket price":
        continue
    else:   
        # totals the ticket sales
        ticket_sales += ticket_cost
        print("Ticket Price: ${:.2f} ".format(ticket_cost))
        ticket_count += 1

    # adds name and ticket price to the initail listd
    all_names.append(name)
    all_tickets.append(ticket_cost)

    # ask user if they want snacks
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snacks = input("Do you want snacks?  ").lower()
        check_snack = string_checker(want_snacks, yes_no_error, yes_no_list)

        # gets order if they want one
        if check_snack == "Yes":
            get_order = get_snack()
        
        else:
            get_order = []

        # fill lists
        for item in snack_lists:
            item.append(0)
            
        # add stuf to the lists if they ask for an order.
        for item in get_order:
            if len(item) > 0:
                to_find = (item[1])
                amount = (item[0])
                add_list = movie_data_dict[to_find]
                add_list[-1] = amount


    
    # finds out amount of tickets left
    ticket_check(ticket_count, MAX_TICKETS)

# figures out profit out side of loop
tiket_profit = ticket_sales - (5 * ticket_count)

# Print information
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and tivket

movie_frame['Sub_total'] = \
    movie_frame['Tickets'] + \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']



movie_frame = movie_frame.reindex(columns=['Popcorn', 'Pita Chips', 'M&Ms', 'Orange Juice', 'Water', 'Sub_total'])
print(movie_frame)

print()
# if youve sold put it prints that
if ticket_count == MAX_TICKETS:
    print("You have sold out")

# if you have not sold out it tells you how many sold and left
else:
    print("You sold {} tickets.".format(ticket_count))
    print("{} spaces remain.".format(MAX_TICKETS - ticket_count))
print()

# shos profit made 
print("Profit: {:.2f}".format(tiket_profit))
