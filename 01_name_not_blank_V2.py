# functions go here

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

# Main routine
name = not_blank("Name: ", "<error> please enter your name")
print()
print(name)