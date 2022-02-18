import random
# random answers
answer_list = ["yes", "no", "ofc", "No you're dumb", "sure", 
"absolutly", "absolutly not", "nope", "dude just stop talking", "maybe", 
"good question", "i don't really know", "lol"]

# main routine
while 1 == 1:
    question = input("Ask a yes/no question -> ")

    if question != "xxx":
        print(random.choice(answer_list))
    else:
        break
