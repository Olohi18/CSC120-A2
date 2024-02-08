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

    def update_price(self, computerID: int, new_os: Optional[str] = None):
        if computerID in self.inventory:
            computer = self.inventory[computerID] # locate the computer
            if int(computer["year made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff
            
    # def refurbish_OS

    #         if new_os is not None:
    #             computer["operating_system"] = new_os # update details after installing new OS
    #     else:
    #         print("Item", item_id, "not found. Please select another item to refurbish.")


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
    computerID = resale.buy(computer1)

    resale.update_price(computerID)
    #resale.sell(computerID)
    


if "__main__" == __name__:
    main()
   