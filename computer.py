class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                description: str,
                processor_type: str,
                hard_drive_capacity: int,
                memory: int,
                operating_system: str,
                year_made: int,
                price: int):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def create_computer(self):
        global itemID
        itemID += 1
        return {itemID: {self.description, self.processor_type, self.hard_drive_capacity, 
                self.memory, self.operating_system, self.year_made, self.price}}    



    #What methods will you need?
    def __str__(self):
        return (f"{self.description}, {self.processor_type}, {self.processor_type}, {self.hard_drive_capacity}, {self.memory}, {self.operating_system}, {self.year_made}, {self.price}") 
    

        
    # def update(self, itemID: int, new_os: str):
    #     if itemID in ResaleShop.inventory:
    #         computer = ResaleShop.inventory[itemID] # locate the computer
    #         if new_os is not None:
    #             computer["operating_system"] = new_os # update details after installing new OS
    #     else:
    #         print("Item", itemID, "not found. Please select another item to refurbish.")
            
        
def main():
    computer1 = Computer("MacAir", "gig", 23, 16, "OS", 2024, 500)
    print(computer1)

if "__main__" == __name__:
    main()
   




