"""Question 1:
Create the class Society with following information:
society_name,house_no_of_mem, flat, income
Methods :
An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class.
"""
class Society():
    def __init__(self,society_name,house_no_of_nem,flat,income):
           
        self.society_name = society_name
        self.house_no_nem = house_no_of_nem
        self.flat = flat
        self.income = income
    def inputData():
        
        data = Society = input("Enter the name of the society:"),
        int(input("Enter the house number:")),
        int(input("Enter the number of members")),
        int(input("Enter your income:"))
        return data 
            
    
    def allocate_flat(self):
        if self.income>=2500:
            self.flat = "A Type"
        elif self.income>=2000 and self.income<=2500:
            self.flat = "B Type"
        elif self.income>=1500 and self.income<=2000:
            self.flat = "C Type"
        else:
            self.flat = "D Type"
        return self.flat
    def show_data(self):
        print(  "SocietyName     : " f"{self.SocietyName}",
                "HouseNoOfMember : " f"{self.HouseNoOfMember}",             
                "Flat            : " f"{self.Flat}",
                "Income          : " f"{self.Income}")
data = Society.inputData()
data.allocate_flat()
data.showdata()


        
        
        
