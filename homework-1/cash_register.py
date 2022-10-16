
"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self, total_items):

        self.total_items = dict(total_items)  # {'item': 'price'}
        self.total_price = 0
        self.discount = .5

    def add_item(self, item, price):
        self.total_items.update({item: price})
        print("Item added:", item)



    def remove_item(self, item):
        self.total_items.pop(item)
        print("Item removed:", item)



    def apply_discount(self):
        discounted_amount = sum(self.total_items.values()) * self.discount
        print(f"Your discount of {self.discount}% has been applied your total is: £{discounted_amount}")
        return discounted_amount


    def get_total(self):
        self.total_price = 0
        return print(f"Your total is: £{sum(self.total_items.values())}")



    def show_items(self):
        print(f"The items in your cart are:{self.total_items}")

    def reset_register(self):
        self.total_items.clear
        self.discount = 0
        self.total_price = 0
        print(f"Register cleared:{self.total_items}")




# EXAMPLE code run:
basket_1 = CashRegister(total_items={'apple': 3.00, 'banana': 1.00, 'mango': 2.30, 'peach': 3.10, 'bread': 1.50})

basket_1.add_item('orange', 2.00)
basket_1.remove_item('apple')
basket_1.get_total()
basket_1.show_items()
basket_1.apply_discount()



