'''
Tayyip Güney 01.03.2022

# Question 2:
# Define a class named ``ItemInfo` with the following description:
# item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)

# Methods :

# A member method calculate_discount() to calculate discount as per the following rules:
# If qty <= 10                —> discount is 0
# If qty (11 to 20 inclusive) —> discount is 15
# If qty >= 20                —> discount is 20

# A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
# A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
# A function show_all() or similar name to allow user to view the content of all the data members.
'''


class ItemInfo():
    
    def __init__(self,item_code=0,item=None, price=None, qty=None, net_price=None, discount=None ) :
        
        self.item_code= item_code
        self.item=item
        self.price=price
        self.qty=qty
        self.net_price= net_price
        self.discount= discount
        
    def buy(self):
        self.item_code=input("Enter the item code : ")
        self.item=input("Enter the item name : ")
        try:
            self.price=float(input(f"Enter the price of {self.item} : "))
            self.qty=float(input(f"Purchase quantity for {self.item} : "))
        except:
            print("\nOOOOPS ! Invalid Value\nPlease enter only numbers\n")
            
            self.price=float(input(f"Enter the price of {self.item} : "))
            self.qty=float(input(f"Purchase quantity for {self.item} : "))

    def calculate_discount(self):
        # discount(Discount percentage on the item)
        if self.qty <= 10 :
            self.discount = 0
        elif 10<self.qty<=20:
            self.discount = 15/100
        elif self.qty>=20:
            self.discount =20/100
        
        self.discount_amount = self.price*self.qty*self.discount
        
        self.net_price = round(self.price*self.qty-(self.discount_amount),2)
        
    def show_all(self):
        
        print(f"\nItem Code     : {self.item_code}\nItem Name     : {self.item}\nItem Price    : $ {self.price}",
              f"\nItem Quantity : {self.qty}\n\nTotal Price   : $ {self.qty*self.price}\nDiscount      :",
              f"$ {self.discount_amount} / (%{int(self.discount*100)})\n\nAmount to be paid : $ {self.net_price}"
              )
while True:
    itm=ItemInfo()
    itm.buy()
    itm.calculate_discount()
    itm.show_all()
    quit=input("\npress 'Q' to exit, press any key to continue : ")
    if quit.lower()=="q":
        break
    
    
    

'''
# Question 2:
# Define a class named ``ItemInfo` with the following description:
# item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)

# Methods :

# A member method calculate_discount() to calculate discount as per the following rules:
# If qty <= 10                —> discount is 0
# If qty (11 to 20 inclusive) —> discount is 15
# If qty >= 20                —> discount is 20

# A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
# A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
# A function show_all() or similar name to allow user to view the content of all the data members.
'''
