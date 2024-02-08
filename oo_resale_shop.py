from typing import Dict, Optional
from computer import Computer


itemID = 0
class ResaleShop:

    # What attributes will it need?
    inventory : {}
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = inventory


    # What methods will you need?
        
    def buy(self, computer: Dict):
        global itemID
        itemID += 1 # increment itemID
        #print(computer)
        self.inventory[itemID] = computer
        #print(self.inventory)
        return itemID
    
    def sell(self, computerID: int):
        if computerID in self.inventory:
            del self.inventory[computerID]
            print("Item", computerID, "sold!")
        else: 
            print("Item", computerID, "not found. Please select another item to sell.")

    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for computerID in self.inventory:
                # Print its details
                print(f'Item ID: {computerID} : {self.inventory[computerID]}')
        else:
            print("No inventory to display.")
        

def main():
    computer1 = Computer("MacAir", "gig", 23, 16, "OS", 2024, 500)
    resale = ResaleShop({})
    resale.print_inventory()
    computerID = resale.buy(computer1)
    resale.print_inventory()
    #resale.sell(computerID)
    


main()