"""
Tayyip Güney 01.03.2022

# Question 3:
# Define a class named Product with the following specifications:

# Data members:

# product_id - A string to store product.
# product_name - A string to store the name of the product.
# product_purchase_price - A decimal to store the cost price of the product.
# product_sale_price - A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
# Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
# Methods :

# A constructor to intialize all the data members with valid default values.
# A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :

# Margin	    Remarks
# <0 (negative)	Loss
# >0 (positive)	Profit

# A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
# A method get_details() that displays all the data members.
"""
class Product():

    def __init__(self) -> None:

        pass

    def set_remarks(self):
        self.margin = self.product_sale_price - self.product_purchase_price
        if self.margin<0:
            self.remark = "Loss"
        elif self.margin>0:
            self.remark = "Profit"
        
    def set_details(self):
        self.product_id = input("Product Id : ")
        self.product_name = input("Product Name : ")
        self.product_purchase_price = float(input("Product purchase price : "))
        self.product_sale_price = float(input("Product sales price : "))
        
        self.set_remarks()
        
    def get_details(self):
        # print("\n")
        print(f"\nProduct Id : {self.product_id}\nProduct Name :  {self.product_name}",
              f"\nPurchase Price : ${self.product_purchase_price}\nSales  Price   : ${self.product_sale_price}",
              f"\nMargin / Remark: ${round(self.margin,2)} / {self.remark}\n",
              )

prod=Product()

prod.set_details()
prod.get_details()



"""

# Question 3:
# Define a class named Product with the following specifications:

# Data members:

# product_id – A string to store product.
# product_name - A string to store the name of the product.
# product_purchase_price – A decimal to store the cost price of the product.
# product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
# Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
# Methods :

# A constructor to intialize all the data members with valid default values.
# A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :

# Margin	    Remarks
# <0 (negative)	Loss
# >0 (positive)	Profit

# A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
# A method get_details() that displays all the data members.
"""