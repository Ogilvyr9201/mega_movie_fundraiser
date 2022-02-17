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