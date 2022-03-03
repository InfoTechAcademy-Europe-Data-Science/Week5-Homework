"""
QUESTİON 2
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)
Methods :
A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all the data members.

"""

class Itemınfo():
    def __self__(self):
        self.item_code   = 0
        self.item_name   = None
        self.price       = 0
        self.qty         = 0
    
    def __init__(self,item_code,item_name,item_price,item_qty,item_discount,item_netPrice):
        self.item_code =item_code
        self.item_name =item_name
        self.item_price = item_price
        self.item_qty = item_qty 
        self.item_discount = item_discount 
        self.item_netPrice = item_netPrice
    

    def calculate_discount(self):
        
        if self.qty >= 20:
            self.discount = 20
        elif self.qty>10 and self.qty < 20:
            self.discount = 15
        else:
            self.discount = 0
        self.net_price = (self.price * self.qty) - self.discount
        return self.discount, self.net_price
        self.discount   = self.price*self.qty
    def buy(self):
        self.item_code = int(input("Enter İtem Code:"))
        self.item_name = input("Enter İtem Name:")
        self.item_price = int(input("Enter the unit price of the ıtmes:"))
        self.item_qty = int(input("How many monts will you purchase:"))
    def show_all(self):
        print(f"İtem code {self.item_code}",
              f"item name {self.item_name}",
              f"item price {self.item_price}",
              f"item qty {self.item_qty}",
              f"item discount{self.item_discount}",
              f"item netprice{self.item_netPrice}")
print(Itemınfo.buy)
print(Itemınfo.calculate_discount)
print(Itemınfo.show_all)

    
     
        
        