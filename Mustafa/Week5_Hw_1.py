class Society():

    # class attribute. Default for every member. 
    # It will change by allocate_flat() method acording to the every member's incom
    flat_type = "A"

    def __init__(self, society_name, house_no_of_mem, flat, income):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income
    
    def allocate_flat(self):
        if 25000 <= self.income:
            Society.flat_type = "A"
            return(f"{self.society_name}'s allocated flat type is {self.flat_type}")
        elif self.income < 25000:
            Society.flat_type = "B"
            return(f"{self.society_name}'s allocated flat type is {self.flat_type}")
        elif self.income < 20000:
            Society.flat_type = "C"
            return(f"{self.society_name}'s allocated flat type is {self.flat_type}")
        else:
            Society.flat_type = "D"
            return(f"{self.flat_type}")
    
    def get_details(self):
        print('Here is the details of the Society:\n'
              'Society name:', self.society_name,
              '\nHouse number:', self.house_no_of_mem,
              '\nFlat Type:', self.flat,
              '\nIncome:', self.income)
              
    def input_data(self):
        self.society_name = input("Enter society name:")
        self.house_no_of_mem = int(input("Enter house number: "))
        self.income = int(input("Enter income: "))

p=Society()
p.input_data()
p.allocate_flat()
p.get_details()