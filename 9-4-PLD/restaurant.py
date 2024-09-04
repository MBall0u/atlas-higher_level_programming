#!/usr/bin/python3
class menu_item:
    def __init__(self, item, price):
        self.item = item
        self.price = price

KP = menu_item("Krabby Patty", 5.99)
HD = menu_item("Hawk Dog", 2.99)

class order:
    def __init__(self):
        self.items = []
    
    def add_items(self, item):
        self.items.append(item)
    
    def calc_total(self):
        total = 0.00
        for i in self.items:
            total += i.price
        total += 1.0875
        return total

new_order = order()
new_order.add_items(HD)
new_order.add_items(KP)
print("{:.02f}".format(new_order.calc_total()))
