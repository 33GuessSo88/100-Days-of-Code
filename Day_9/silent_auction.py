
# list_of_bids = []
# more_bids = True

# while more_bids == True:
#     input_name = input("What is your name?\n")
#     input_bid = int(input("What is your bid?\n$"))

    

#     list_of_bids.append({"name": input_name, "bid": input_bid})

#     more_bids = input("Are there more users - yes or no?\n")
#     if more_bids == "no":
#         more_bids = False
#     else:
#         more_bids = True
#     print(list_of_bids)

# max_bid = 0
# max_bid_name = ""
# for dict in list_of_bids:
#     if dict["bid"] > max_bid:
#         max_bid = dict["bid"]
#         max_bid_name = dict["name"]

# print(f"The highest bid is ${max_bid} by {max_bid_name}")

#I have no idea why I made this a list of dictionaries. STUPID. 
#It only needs to be a dictionary with multiple keys and values.
#I should re-do this exercise again from scratch without using a list


#This is my second try using only dictionary
#I struggled with thinking I had to have name and bid in the dictionary.
#NO - the dict is just a key value pair of names and bids, you don't have to label them
#Found the .items method - very handy

dict_of_bids = {}
keep_bidding = True


def find_highest_bidder(bids):
    highest_bid = 0
    highest_bidder = ""
    for key, value in dict_of_bids.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidder = key
    print(f"The highest bid is ${highest_bid} by {highest_bidder}")

while keep_bidding == True:
    input_name = input("What is your name? ")
    input_bid = int(input("What is your bid? $"))

    dict_of_bids[input_name] = input_bid
    more_bidders = input("Are there more bidders? yes or no ")
    if more_bidders == "no":
        keep_bidding = False
        find_highest_bidder(dict_of_bids)



