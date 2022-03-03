"""
Tayyip Güney 03.03.2022

# Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.

# Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()

# calculate_discount():

# total_price = price * qty
# discount —> 25% if total_price >= 4000
# discount —> 15% if total_price >= 2000
# discount —> 10% if total_price < 2000
# price_tobe_paid = total_price - discount
# shopping_cart():

# Let user add items in the shopping basket. Be creative with the items, set their prices as well.

# __str__():

    # Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
    # Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in 
    # __init__() and pass customer information as arguments while creating a customer object.

# __str__():

# Print customer information and price nicely. Find a way to link two classes. 
# For example, instances of both classes may have a customer number. 
# With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. 
# So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number 
# such as price, quantity or so.

# In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.

# Simple example:

# Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
# shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
# Crate a few customers and print their information (Personal and shopping info).
# """

from random import randint

class Customer():
    
    def __init__(self) -> None:
        
        pass

    def show_customer(self):
        print("Name        : ",self.first_name)
        print("Last Name   : ",self.last_name)
        print("Adress      : ",self.adress)
        print("Customer ID : ",self.customer_id)
        
        
    def get_cust_info(self):
        self.call       = input("Mr./Ms./Mrs.: ")
        self.first_name       = input("First Name  : ")
        self.last_name  = input("Last Name   : ")
        self.adress     = input("Adress      : ")
        self.customer_id = str(randint(0,999))+str(randint(0,999)) # for random customer id
    
class Items(Customer):
    shop_items_dic={} 
    cust_list=[]

    def __init__(self) -> None:
        pass
    
    def calculate_discount(self):
        if self.total_price >=4000:
            self.discount = 25/100
        elif self.total_price>=2000:
            self.discount=15/100
        elif self.total_price<2000:
            self.discount=10/100     
            
        self.get_total_amount() # call function for final result
        
    def shopping_cart(self):
        """Let user add items in the shopping basket. Be creative with the items, set their prices as well."""
        
        self.total_price=0
        while True: 
            
            self.item_name=input("\nItem Name     : ")
            self.item_price=float(input("Item Price    : "))
            self.item_qty=int(input("Item quantity : "))
            
            self.total_price += (self.item_price*self.item_qty)   # calculate total price
            
            Items.cust_list.append([self.item_name,self.item_price,self.item_qty]) # items go to list (cust_list)
            Items.shop_items_dic.update({self.customer_id : Items.cust_list})      # list goes to dictionary (shop_items_dic) We have added it to the dictionary to improve it in the future.
            
            qu=input("\npress 'Q' to EXIT , press any key to NEW ITEM : ")  # Will it add new item?
            
            if qu.lower()=="q":
                Items.cust_list=[]
                break
            
        self.calculate_discount()

    def get_total_amount(self):
        
        self.price_tobe_paid = self.total_price - (self.total_price*self.discount)
 
    def __str__(self):
        s=""
        for i in Items.shop_items_dic.get(self.customer_id): # let's get the products from the list in the dictionary
            s+=f"\n    {i[1]}             {i[2]}                                  $ {i[1]*i[2]}"  
        return f"""

SHOPPING CARD 

Customer Id : {self.customer_id}
-------------------------------------------------------------------
    Price             Quantitiy                      Total per unit
   -------           -----------                     --------------
   
"""+s+f"""


    Subtotal                                          =  $ {self.total_price}
    Discount                                          =  $ {round(self.total_price*self.discount,2)} (%{self.discount*100})                                                                   
    ---------------------------------------------------------------
    TOTAL                                             =  $ {self.price_tobe_paid}
    
    
    {self.call}. {self.first_name} {self.last_name}
    {self.adress}
    
-------------------------------------------------------------------              
"""
        
while True:
    item_e=Items()
    item_e.get_cust_info()
    item_e.shopping_cart()
    print(item_e)
    new_customer=input("\n  Will there be new customer login?\n\npress 'Y' for Yes, press any key to EXIT : ")
    
    if new_customer.lower()!="y":    
        break



"""
# Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.

# Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()

# calculate_discount():

# total_price = price * qty
# discount —> 25% if total_price >= 4000
# discount —> 15% if total_price >= 2000
# discount —> 10% if total_price < 2000
# price_tobe_paid = total_price - discount
# shopping_cart():

# Let user add items in the shopping basket. Be creative with the items, set their prices as well.

# __str__():

    # Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
    # Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in 
    # __init__() and pass customer information as arguments while creating a customer object.

# __str__():

# Print customer information and price nicely. Find a way to link two classes. 
# For example, instances of both classes may have a customer number. 
# With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. 
# So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number 
# such as price, quantity or so.

# In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.

# Simple example:

# Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
# shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
# Crate a few customers and print their information (Personal and shopping info).
# """