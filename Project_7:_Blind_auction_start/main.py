import os
from art import logo

print(logo)

bid_record = {}
another_bid = "yes"

while another_bid == "yes":
  name = input("What is your name : ")
  bid_ammount = input("Enter the bid amount: $ ")
  bid_record[name] = bid_ammount
  another_bid = input("Is there other user who wnat to bid (Yes/No): ").lower()
  if another_bid == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')  #cross-platform clear

highest_bid = 0
winner = ""
for key in bid_record:
  if int(bid_record[key]) > int(highest_bid):
    winner = key
    highest_bid = bid_record[key]
print(f"The winner is {winner} with the bidding amount of ${highest_bid}")
