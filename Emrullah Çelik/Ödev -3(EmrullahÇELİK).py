"""Question 3:
Define a class named Product with the following specifications:
Data members:

product_id – A string to store product.
product_name - A string to store the name of the product.
product_purchase_price – A decimal to store the cost price of the product.
product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :

A constructor to intialize all the data members with valid default values.
A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
![h51](https://user-images.githubusercontent.com/98665012/155852165-694f473b-c1b2-4f35-8cac-74e1db4e6d86.png)

A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
A method get_details() that displays all the data members.
"""

class Product:
    def __init__(self, product_id = 0, product_name = "", product_purchase_price = 0, product_sale_price = 0) -> None:
        self.product_id = product_id # ürünü depolamak için
        self.product_name = product_name # ürünün adını depolak için
        self.product_purchase_price = float(product_purchase_price) # maliyet fiyatı ondalık fiyatı
        self.product_sale_price = float(product_sale_price)
        
    
    def input_data(self):
        self.product_id = int(input("Enter your Product ID: "))
        self.product_name = input("Enter your Product Name: ")
        self.product_purchase_price = int(input("Enter your Product Purchase Price: "))
        self.product_sale_price = int(input("Enter your Product sale price: "))
        self.marj = self.product_sale_price - self.product_purchase_price


    def set_remarks(self):
        if self.marj > 0:
            return "Profit"
        elif self.marj < 0:
            return "Loss"
            

    def get_details(self):
        return f"\n\
            Product ID          :   {self.product_id}\n\
            Product Name        :   {self.product_name}\n\
            Purchase Price      :   {self.product_purchase_price}\n\
            Product Sale Price  :   {self.product_sale_price}\n\
            Remarks             :   {self.set_remarks()}\n\
         -----------------------------------------------------------"
        
        
        
        
        





product = Product()
product.input_data()
print(product.get_details())