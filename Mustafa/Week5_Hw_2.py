"""Week5 Homework 2 - Discount -"""

class ItemInfo:
    def __init__(self):
        pass

    def buy(self):
        self.item_code = input("Please enter item code: ")
        self.item = input("Please enter item name: ")
        self.price = float(input("Please enter price of item: "))
        self.qty = int(input("Please enter quantity: "))
    
    def calculate_discount(self):
        #less than 10 item discount will be 0
        if self.qty <= 10:
            new_price = 1
        
        #buying between 11-20 items diserve %15 discount
        elif 11 <= self.qty < 20:  
            new_price = 0,85  
        
        #more than 20 items get %20 discount
        else :
            new_price = 0,8
            return float(self.price * new_price)
    
    def show_all(self):
        print("\nItem Code:     ", self.item_code,"\nItem:          ", self.item, "\nItem UVP price :", self.price)
        print("Discounted item price: ", self.calculate_discount())

while True:
    trade = ItemInfo()
    trade.buy()
    trade.calculate_discount()
    trade.show_all()
    quit = input("\nWhen your purchase ends please press 'e' to exit : ")
    if quit.lower()=="e":
        break
    
    