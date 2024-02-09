
#Defines the computer class
class Computer:

    # Attributes of class Computer
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # Initializes constructor for the Computer class
    def __init__(self,
                description: str,
                processor_type: str,
                hard_drive_capacity: int,
                memory: int,
                operating_system: str,
                year_made: int,
                price: int):
        #Assigns the attribute x to variable self.x
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    #Prints the created Computer instances
    def __str__(self):
        return (f"{self.description}, {self.processor_type}, {self.hard_drive_capacity}, {self.memory}, {self.operating_system}, {self.year_made}, {self.price}") 
    
    #Returns the year associated with a given computer instance--- not necessary for now
    def year_made(self):
        return (self.year_made)
            
#main() program to test the Computer class       
def main():
    #Creates a Computer instance, computer1
    computer1 = Computer("MacAir", "gig", 23, 16, "OS", 2024, 500) 
    print(computer1)


#Prevents function from running when imported to another function
if "__main__" == __name__:
    main()
   




