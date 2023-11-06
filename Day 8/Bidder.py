from click import clear


bids = {}
bid_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bid_finished:
    name = input("Enter your name \n")
    bid_price = int(input("Enter your bid price"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if should_continue == "no":
        bid_finished = True
        find_highest_bidder(bids)
    if should_continue == "yes":
        clear()
