import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

auction = {}
winner = ""
bid =  True

def highest_bidder(all_bids):
  max_bid = 0
  price = 0
  for key in all_bids:
    price = all_bids[key]

    if int(price) > int(max_bid):
      winner = key
      max_bid = price

  print(f"{winner} is the winner with a bid of ${max_bid}")

while(bid):
  name = input("Input your name: ")
  price = input("Enter your bid: $")
  auction[name] = price
  end = input("Are their more bidders? Y or n: ")

  if end.lower() == "n":
    bid = False

highest_bidder(auction)