"""
Question 2:
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock)
discount(Discount percentage on the item), net_price(Price after discount)

Methods :
A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty. 
Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
    A function show_all() or similar name to allow user to view the content of all the data members.
"""


class ItemInfo:
    def __init__(self, item_Name = "", price = 0, qyt = 0, item_code = 0 ) -> None:
        self.item_Name = item_Name
        self.price = int(price)
        self.qyt = int(qyt)
        self.item_code = item_code

    def input_data(self):
        self.item_Name = input("Please enter the name of the product you want to buy: ")
        self.price = int(input("Please enter the price of the product you want to buy: "))        
        self.qyt = int(input("Please enter the quantity of the product you want to buy: "))
        self.item_code = int(input("Please enter the code of the product you want to buy: "))

    def calculate_discount(self):
        if self.qyt <= 10:
            return 0   
        elif 11 <= self.qyt < 20:
            return (int(self.price) * int(self.qyt)) * (15/100)
        else:
            return (int(self.price) * int(self.qyt)) * (20/100)
    
    def buy(self):
        return (int(self.price) * int(self.qyt)) - int(self.calculate_discount())

    def show_all(self):
        return f"\n\
            The Product You Want to Buy                 :   {self.item_Name}\n\
            The Code of The Product You Want to Buy     :   {self.item_code}\n\
            The Price of The Product You Want to Buy    :   {self.price}\n\
            The Quantity of The Product You Want to Buy :   {self.qyt}\n\
            Discount Amount You Have Earned             :   {self.calculate_discount()}\n\
          -------------------------------------------------------------------------------------\n\
            Net Amount You Have to Pay                  :   {self.buy()}"



shopping = ItemInfo()
shopping.input_data()

print(shopping.show_all())

