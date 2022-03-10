import random
# random answers
answer_list = ["OJ", "June", "Beniju", "Sir Tag", "Clash with Ash", 
"Kent", "ClashArt", "YoSoyRick", "Grax", "Jojonas", 
"Ouahleouff", "Artube Clash", "lol"]

# main routine
while 1 == 1:
    question = input("Ask a yes/no question -> ")

    if question != "xxx":
        print(random.choice(answer_list))
    else:
        break
