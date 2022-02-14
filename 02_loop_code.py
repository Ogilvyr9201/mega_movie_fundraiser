name = ""
count = 0
max_tickets = 5

while name != "xxx"  and count < max_tickets:

    # Get details
    name = input("Name: ")
    count += 1
    tickets_left = max_tickets - count
    print("You have {} seats left".format(tickets_left))
    if tickets_left == 0:
        print("YOu have sold out")