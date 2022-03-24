import pandas
# initialise snack lists

all_names = ['Rangi', 'Mania', 'Talia', 'Arihi', 'Fetu']

popcorn = []
mms = []
pita_chips = []
water = []
tenth_place = []

snack_lists = [popcorn, mms, pita_chips, water, tenth_place]


# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Water': water,
    'Tenth Place': tenth_place
    
}


test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Tenth Place']],
    [[]],
    [[1, 'Water']],
    [[1, 'Popcorn'], [1, 'Tenth Place']],
    [[1, 'Pita Chips'], [1, 'Tenth Place'], [2, 'M&Ms']]
]

count = 0
for client_order in test_data:

    # assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    # print (snack_lists)

    # get order = test_data[count]
    snack_order = test_data[count]

    print("snack order", snack_order)
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print()
print("Popcorn: ", snack_lists[0])
print("M&Ms: ", snack_lists[1])
print("Pita Chips : ", snack_lists[2])
print("Water: ", snack_lists[3])
print("Orange Juice: ", snack_lists[4])
print()

# Print information
movie_frame = pandas.DataFrame(movie_data_dict)

movie_frame = movie_frame.set_index('Name')

movie_frame = movie_frame.reindex(columns=['Popcorn', 'Pita Chips', 'M&Ms', 'Tenth Place', 'Water'])

print(movie_frame)