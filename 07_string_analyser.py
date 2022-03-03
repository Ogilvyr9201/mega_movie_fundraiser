import re

# works out weather string has numbers 
# and seperates string into amount and item 

test_strings = [
    "popcorn",
    "2 pc",
    "1.5OJ",
    "4OJ"
]


for item in test_strings: 

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # if item has a number separate it into two parts (number and item)
    if re.match(number_regex, item):
        amount= int(item[0])
        desired_snack = item[1:]

    # if item does not have a number infront, set number too 1
    else:
        amount = 1
        desired_snack = item

    # remove white space around snack
    desired_snack = desired_snack.strip()

    print("Amount", amount)
    print("Snack:", desired_snack)
    print("Length of snack:", len(desired_snack))
    print()
