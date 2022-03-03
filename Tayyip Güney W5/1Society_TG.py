'''
Tayyip Güney 01.03.2022

# Question 1:
# Create the class Society with following information:

# society_name,house_no_of_mem, flat, income

# Methods :

# An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
# input_data() To read information from members
# allocate_flat() To allocate flat according to income using the below table.
# show_data() to display the details of the entire class.

# Income	            Flat
# >=25000	            A Type
# >=20000 and <25000	B Type
# >=15000 and <20000	C Type
# <15000	            D Type

'''

class Society:
    
    def __init__(self) :
    
        # self.input_data() # Performs the action when the object is defined, 
                               ## without calling the input_data() function outside
        pass
        
    def input_data(self):
        
        self.society_name = input("Enter the member's name : ")
        self.house_no_of_mem = input("Enter the house number : ")
        try:
            self.income = int(input("Enter the income : "))
        except:
            print("\nOppps! Invalid Value\nPlease enter only numbers\n")
            self.income = int(input("Enter the income : "))
            
        self.allocate_flat()  # call the function that finds the flat
        # self.show_data()      # call the show_data function
        
    def allocate_flat(self):
        if self.income>=25000:
            self.flat = "A Type"
            
        elif 20000<=self.income<25000:
            self.flat = "B Type"
            
        elif 15000<=self.income<20000:
            self.flat = "C Type"
            
        elif self.income<15000:
            self.flat = "D Type"
            
    def show_data(self):
        print(f"\nSociety name : {self.society_name}\nHouse no : {self.house_no_of_mem}",
              f"\nIncome of member : {self.income}\nFlat Type to member : {self.flat}\n")
        

soc1=Society()

soc1.input_data()    # if the input_data() function in __init__() is open, this line should be closed

soc1.show_data()     # if the show_data() function in input_data() is open, this line should be closed



'''
# Question 1:
# Create the class Society with following information:

# society_name,house_no_of_mem, flat, income

# Methods :

# An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
# input_data() To read information from members
# allocate_flat() To allocate flat according to income using the below table.
# show_data() to display the details of the entire class.

# Income	            Flat
# >=25000	            A Type
# >=20000 and <25000	B Type
# >=15000 and <20000	C Type
# <15000	            D Type

'''