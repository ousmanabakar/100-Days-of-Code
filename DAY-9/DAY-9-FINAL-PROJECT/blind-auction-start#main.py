from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
name_bid_dict ={}
while True:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))

  name_bid_dict[name]=price
  
  print(name_bid_dict)
  response =input("Are there any other bidders? Type 'yes or 'no'.").lower()
  
  if response == "yes":
    clear()

  else:
    new_name=""
    max_bid=0

    for key, value in name_bid_dict.items():
      if value>max_bid:
        max_bid=value
        if name_bid_dict[key] == max_bid:
          new_name=key
    print(f"The winner is {new_name} with a bid of ${max_bid}")
    break
