"""
Question 3:
Define a class named Product with the following specifications:
Data members:
product_id - A string to store product.
product_name - A string to store the name of the product.
product_purchase_price - A decimal to store the cost price of the product.
product_sale_price - A decimal to store 
Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
A constructor to intialize all the data members with valid default values.
A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
A method get_details() that displays all the data members.
https://user-images.githubusercontent.com/98665012/155852494-f010eb3e-4782-46b8-9d32-a1750e575347.png
"""
class Product():
    def __init__(self,product_id, product_name,product_purchase_price,product_sale_price):
        self.product_id = product_id
        self.product_name=product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.Margin = (self.product_sale_price)-(self.product_purchase_price)
    def remarks(self):
        if self.Margin<0:
            return "Loss" 
        elif self.Margin>0:
            return "Profit"
    def set_details(self):
        a = self.product_id = int(input("Enter Product Id:"))
        b = self.product_name = input("Enter Product Name:")
        c = self.product_purchase_price = int(input("Enter Product Purcahse Price:"))
        d = self.product_sale_price = int(input("Enter Product Sales Price:"))
        return a,b,c,d 
    def get_details(self):
        print(f"""Product_id                : {self.product_id}
                  Product_name              : {self.product_name}
                  Product_purchase_price    : {self.product_purchase_price}
                  Product_sale_price        : {self.product_sale_price}        
                                                                      """ )
print(Product.get_details())
print(Product.set_details)
