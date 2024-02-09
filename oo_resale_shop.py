#Imports from the typing module methods Dict and Optional
from typing import Dict, Optional
#Imports the class Computer from file with filename computer.py in the folder
from computer import Computer

itemID = 0 #Sets itemID to 0, increments it by 1 after every computer instance is added


#Defines the ResaleShop class
class ResaleShop:

    #Initializes the required attribute for the ResaleShop class
    inventory : Dict[int, Dict] = {}
    def __init__(self, inventory):
        self.inventory = inventory

    #Defines the buy function to add an item to the inventory    
    def buy(self, computer: Dict):
        global itemID
        itemID += 1 # increment itemID
        #print(computer)
        self.inventory[itemID] = computer
        #print(self.inventory)
        return itemID
    
    #Defines the sell function to remove an item from the inventory   
    def sell(self, computerID: int):
        if computerID in self.inventory:
            del self.inventory[computerID]
            print("Item", computerID, "sold!")
        else: 
            print("Item", computerID, "not found. Please select another item to sell.")


    #Prints items in the inventory
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for computerID in self.inventory:
                # Print its details
                print(f'Item ID: {computerID}, Properties: ({self.inventory[computerID]})')
        else:
            print("Inventory currently empty. No inventory to display.")

#Program parts I really need help with
#Whenever I try running the update_price, it says computer object "price" cannot be assigned
    """def update_price(self, computerID: int, new_price: int):
        if computerID in self.inventory:
            self.inventory[computerID]["price"] = new_price
        else:
            print("Item", computerID, "not found. Cannot update price.")"""
    
#Similarly, running this function says Computer object not subscriptable
    """def refurbish(self, computerID: int, new_os: Optional[str] = None):
    if computerID in self.inventory:
        computer = self.inventory[computerID] # locate the computer
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff

        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS
    else:
        print("Item", computerID, "not found. Please select another item to refurbish.")"""
    

#main functin that implements the methods defined in the ResaleShop class
def main():
    #Creates two computers, computer1 and computer2
    computer1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)
    computer2 = Computer("MacAir", "3.5 GHc 12-Core Intel Neon F6", 512, 256,"macOS Big Sur", 2023, 1500)
    
    #Creates an instance of the ResaleShop class
    resale = ResaleShop({})
    print("-----Loading inventory------")
    resale.print_inventory() #prints items in inventory

    print("-----Buying 1st computer-----")
    computerID = resale.buy(computer1) #adds computer1 to inventory

    print("-----1st Computer bought-----")
    print()
    resale.print_inventory() #prints items in inventory

    print("----Buying second computer----")
    computerID = resale.buy(computer2) #adds computer2 to inventory

    print("-----2nd Computer bought-----")
    print()
    resale.print_inventory() #prints items in inventory
    
    print("-----Selling computer 1-----")
    resale.sell(1) #Sells computer1

    print() #prints a new line
    print("----items left in inventory:-----")
    resale.print_inventory() #prints items in inventory
    

#Runs main function but prevents main() from running when package is imported to another program
if "__main__" == __name__:
    main()
   