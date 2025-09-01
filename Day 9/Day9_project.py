import art

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winnder is {winner} with a bid of {highest_bid}")

bids = {}

bidding = True

while (bidding):
    print(art.logo)

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bids[name] = bid

    if input("Are there any other bidders? Type 'yes' or 'no'\n").lower() == "no":
        bidding = False
        find_highest_bidder(bids)

    print("\n" * 50)








    

# max = next(iter(bidders))
# for key in bidders:
#     if bidders[key] > bidders[max]:
#         max = key
    
# print(f"The winner is {max} with a bid of ${bidders[max]}")