
dict1={}
def highest_bidder(dict2):
    highest_bid=0
    winner = ""
    for bidder in dict2:
        bid_amount=dict2[bidder]#bidder:value
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"Winner of the auction is {winner} with an amount of {highest_bid}")
continue1=True
while continue1:
    name=input("What is your name:")
    bid=int(input("What's your bid amount:"))
    dict1[name]=bid#Angela:2300
    choice=input("Is there any other bidders?Type 'yes' or 'no'::").lower()
    if(choice=='no'):
        continue1=False
        highest_bidder(dict1)
    elif(choice=='yes'):
        print("\n")


        
        
        