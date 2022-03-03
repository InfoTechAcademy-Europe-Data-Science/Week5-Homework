"""# Week5-Homework
Question 1:
Create the class Society with following information:
society_name,house_no_of_mem, flat, income

Methods :
An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class.
![h5](https://user-images.githubusercontent.com/98665012/155852098-3b9c4c90-149e-4685-8cb1-44001a6088bc.png)"""


class Society:
    def __init__(self, society_name = '', income = 0, houseNoOfNem = 0) -> None:
        self.society_name = society_name
        self.houseNoOfNem = int(houseNoOfNem)
        self.income = int(income)

    def input_data(self):
        self.society_name = input("Enter a Society Name: ")
        self.income = int(input("Enter your income please: "))
        self.houseNoOfNem = int(input("Enter your House Number: "))  

    def allocate_flat(self):
        if self.income >= 25000:
            return "Type A"
        elif 25000 > self.income >= 20000:
            return "Type B"
        elif 20000 > self.income >= 15000:
            return "Type C"
        else:
            return "Type D"
    
    def show_data(self):
        return f"\n\
        Your society name is    :   {self.society_name}\n\
        Your Sallary            :   {self.income}\n\
        Your House No of Mem    :   {self.houseNoOfNem}\n\
        Your flat type          :   {self.allocate_flat()}"





house = Society()
house.input_data()
print(house.show_data())