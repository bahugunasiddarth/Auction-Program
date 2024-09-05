import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

#For Clear
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

bids= {}

budding_finishing = False



def find_highest_bidder(bidder_record):
    highest_bid= 0
    winner=""

    for bidder in bidder_record:
        bid_amount= bidder_record[bidder]
        if bid_amount> highest_bid:
            highest_bid = bid_amount
            winner= bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        


while not budding_finishing :
    name= input("what is your name? ")
    price= int(input("What is you bid price $? "))
    #create dictionary
    bids[name]=price
    should_continue= input("Are there is any other bidders? 'yes' or 'no'.")
    if should_continue == "no":
        budding_finishing = True
        find_highest_bidder(bids)
    else:
        clear()  
