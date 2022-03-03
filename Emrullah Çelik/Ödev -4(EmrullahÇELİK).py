"""Question 4:
Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()

calculate_discount():
total_price = price * qty
discount —> 25% if total_price >= 4000
discount —> 15% if total_price >= 2000
discount —> 10% if total_price < 2000
price_tobe_paid = total_price – discount

shopping_cart():
Let user add items in the shopping basket. Be creative with the items, set their prices as well.

__str__():
Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.

__str__():
Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.

In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
Simple example:

Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
Crate a few customers and print their information (Personal and shopping info)."""


class Customer:
    def __init__(self, customerName = "", customerSurname = "", customerId = 0) -> None:
        self.customerName = customerName
        self.customerSurname = customerSurname
        self.customerId = customerId
    
    def input_data(self):
        self.customerName = input("Enter Customer Name: ")
        self.customerSurname = input("Enter Customer Surname: ")
        self.customerId = int(input("Enter Customer ID: "))

class Item(Customer): 
    def __init__(self, price = 0, qyt = 0, item = "") -> None:
        Customer.input_data(self)
        self.price = float(price)
        self.qyt = int(qyt)
        self.item = item

    def add_data(self):
        self.item = input("Enter an item name: ")
        self.price = float(input("Enter price: "))
        self.qyt = int(input("Enter quantity: "))
        self.total_price = float(self.price) * int(self.qyt)
    
    def shopping_Card(self):
        return self.item
        
    def calculate_discount(self):
        if self.total_price >= 4000:
            return self.total_price * 0.25
        elif 4000 > self.total_price >= 2000:
            return self.total_price * 0.15
        else:
            return self.total_price * 0.15
    
    def get_total_amount(self):
        return self.total_price - self.calculate_discount()

    def __str__(self) -> str:
        return f"\n\
            Customer Name and Surname   :   {self.customerName} {self.customerSurname}\n\
            Customer ID                 :   {self.customerId}\n\
            ----------------------SHOPPİNG CARD---------------------------\n\
            Customer ID                 :   {self.customerId}\n\
            Item                        :   {self.shopping_Card()}\n\
            Item Price                  :   {self.price}\n\
            Quantity                    :   {self.qyt}\n\
            Total Price                 :   {self.total_price}\n\
            Discount                    :   {self.calculate_discount()}\n\
            ------------------------NET PRİCE-----------------------------\n\
            Net Price                   :   {self.get_total_amount()}"



result2 = Item()
result2.add_data()
print(result2) 




