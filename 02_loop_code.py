name = ""
count = 0
max_tickets = 5

while name != "xxx"  and count < max_tickets:

    # Get details
    name = input("Name: ")

    # If exit code is not input
    if name != "xxx":
        count += 1
        tickets_left = max_tickets - count
        # checks if there is only 1 space left
        if tickets_left == 1:
            print("THERE IS ONE SPACE LEFT!")
        else:
            print("You have {} seats left".format(tickets_left))

# Print results of loop
print()
# if youve sold put it prints that
if tickets_left == 0:
    print("You have sold out")

# if you have not sold out it tells you how many sold and left
else:
    print("You sold {} tickets.".format(count))
    print("{} spaces remain.".format(tickets_left))
print()
