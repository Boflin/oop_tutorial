# https://www.youtube.com/watch?v=Ej_02ICOIgs&ab_channel=freeCodeCamp.org
# Following this OOP Tutorial on youtube!


class Item():
    pay_rate = 0.8 # The pay rate after a 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        # Validating the received arguments to make sure it's correct
        assert price >= 0, f"Price ({price}) must be greater than 0"
        assert quantity >= 0, f"Quantity ({quantity}) must be greater than 0"

        # Assigning self objects
        print(f"Initialized the following: {name}. Price: ${price}. Quantity: {quantity}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 12)
item2 = Item("Laptop", 1000, 22)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
