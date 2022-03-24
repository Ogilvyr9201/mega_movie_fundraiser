import pandas
# initialise snack lists

all_names = ['Rangi', 'Mania', 'Talia', 'Arihi', 'Fetu']
all_tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

popcorn = []
mms = []
pita_chips = []
water = []
tenth_place = []

snack_lists = [popcorn, mms, pita_chips, water, tenth_place]


# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Tickets': all_tickets,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Water': water,
    'Tenth Place': tenth_place
    
}

# price dictionary
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Tenth Place': 3.25
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
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount



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
    movie_frame['Tenth Place']*price_dict['Tenth Place']



movie_frame = movie_frame.reindex(columns=['Popcorn', 'Pita Chips', 'M&Ms', 'Tenth Place', 'Water', 'Sub_total'])
print(movie_frame)
